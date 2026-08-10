"""Graphics view with zoom, panning, palette drops and host-owned actions."""

from __future__ import annotations

from PySide6.QtCore import QPoint, Signal, Qt
from PySide6.QtGui import QKeySequence, QPainter
from PySide6.QtWidgets import QGraphicsView, QMenu

from node_editor.items import NodeItem
from node_editor.palette import INSTRUCTION_MIME_TYPE
from node_editor.style import MAX_ZOOM, MIN_ZOOM


class NodeView(QGraphicsView):
    zoomChanged = Signal(int)
    instructionDropped = Signal(str, float, float)
    copyRequested = Signal(object)
    deleteRequested = Signal(object)
    runSingleRequested = Signal(object)
    runFromRequested = Signal(object)

    def __init__(self, scene_, parent_=None):
        super().__init__(scene_, parent_)
        self._zoom = 1.0
        self._panning = False
        self._pan_start = QPoint()
        self._pan_moved = False
        self._instruction_types: set[str] = set()
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing
            | QPainter.RenderHint.TextAntialiasing
            | QPainter.RenderHint.SmoothPixmapTransform
        )
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)
        self.setAcceptDrops(True)
        self.setFrameShape(QGraphicsView.Shape.NoFrame)

    def set_instruction_types(self, type_ids_) -> None:
        self._instruction_types = {str(type_id_) for type_id_ in type_ids_}

    def wheelEvent(self, event_):
        factor_ = 1.15 if event_.angleDelta().y() > 0 else 1.0 / 1.15
        new_zoom_ = max(MIN_ZOOM, min(self._zoom * factor_, MAX_ZOOM))
        if new_zoom_ != self._zoom:
            self.scale(new_zoom_ / self._zoom, new_zoom_ / self._zoom)
            self._zoom = new_zoom_
            self.zoomChanged.emit(round(self._zoom * 100))
        event_.accept()

    def mousePressEvent(self, event_):
        if event_.button() == Qt.MouseButton.RightButton:
            self._panning = True
            self._pan_moved = False
            self._pan_start = event_.position().toPoint()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            event_.accept()
            return
        super().mousePressEvent(event_)

    def mouseMoveEvent(self, event_):
        if self._panning:
            current_position_ = event_.position().toPoint()
            delta_ = current_position_ - self._pan_start
            if delta_.manhattanLength() > 2:
                self._pan_moved = True
            self._pan_start = current_position_
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - delta_.x()
            )
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - delta_.y()
            )
            event_.accept()
            return
        super().mouseMoveEvent(event_)

    def mouseReleaseEvent(self, event_):
        if event_.button() == Qt.MouseButton.RightButton and self._panning:
            self._panning = False
            self.unsetCursor()
            event_.accept()
            return
        super().mouseReleaseEvent(event_)

    def dragEnterEvent(self, event_):
        if self._drop_type(event_) is not None:
            event_.acceptProposedAction()
            return
        super().dragEnterEvent(event_)

    def dragMoveEvent(self, event_):
        if self._drop_type(event_) is not None:
            event_.acceptProposedAction()
            return
        super().dragMoveEvent(event_)

    def dropEvent(self, event_):
        type_id_ = self._drop_type(event_)
        if type_id_ is not None:
            scene_position_ = self.mapToScene(event_.position().toPoint())
            self.instructionDropped.emit(
                type_id_, float(scene_position_.x()), float(scene_position_.y())
            )
            event_.acceptProposedAction()
            return
        super().dropEvent(event_)

    def _drop_type(self, event_) -> str | None:
        if not event_.mimeData().hasFormat(INSTRUCTION_MIME_TYPE):
            return None
        try:
            type_id_ = bytes(
                event_.mimeData().data(INSTRUCTION_MIME_TYPE)
            ).decode("utf-8")
        except UnicodeDecodeError:
            return None
        if self._instruction_types and type_id_ not in self._instruction_types:
            return None
        return type_id_ or None

    def _node_at(self, viewport_position_) -> NodeItem | None:
        item_ = self.itemAt(viewport_position_)
        while item_ is not None and not isinstance(item_, NodeItem):
            item_ = item_.parentItem()
        return item_ if isinstance(item_, NodeItem) else None

    def contextMenuEvent(self, event_):
        if self._pan_moved:
            self._pan_moved = False
            event_.accept()
            return
        node_ = self._node_at(event_.pos())
        if node_ is None or node_.is_terminal:
            super().contextMenuEvent(event_)
            return
        if not node_.isSelected():
            self.scene().clearSelection()
            node_.setSelected(True)
        selected_ids_ = self.scene().selected_command_ids()
        if not selected_ids_:
            return

        menu_ = QMenu(self)
        copy_action_ = menu_.addAction("复制")
        copy_action_.setShortcut(QKeySequence.StandardKey.Copy)
        delete_action_ = menu_.addAction("删除")
        delete_action_.setShortcut(QKeySequence.StandardKey.Delete)
        run_single_action_ = None
        run_from_action_ = None
        if len(selected_ids_) == 1:
            menu_.addSeparator()
            run_single_action_ = menu_.addAction("运行此指令")
            run_from_action_ = menu_.addAction("从此指令运行")
        selected_action_ = menu_.exec(event_.globalPos())
        if selected_action_ == copy_action_:
            self.copyRequested.emit(selected_ids_)
        elif selected_action_ == delete_action_:
            self.deleteRequested.emit(selected_ids_)
        elif selected_action_ == run_single_action_:
            self.runSingleRequested.emit(selected_ids_[0])
        elif selected_action_ == run_from_action_:
            self.runFromRequested.emit(selected_ids_[0])
        event_.accept()

    def keyPressEvent(self, event_):
        selected_ids_ = self.scene().selected_command_ids()
        if event_.matches(QKeySequence.StandardKey.Copy) and selected_ids_:
            self.copyRequested.emit(selected_ids_)
            event_.accept()
            return
        if event_.key() == Qt.Key.Key_Delete and selected_ids_:
            self.deleteRequested.emit(selected_ids_)
            event_.accept()
            return
        super().keyPressEvent(event_)

    def fit_graph(self):
        fitted_rect_ = self.scene().graph_items_rect()
        self.fitInView(fitted_rect_, Qt.AspectRatioMode.KeepAspectRatio)
        fitted_zoom_ = self.transform().m11()
        self._zoom = max(MIN_ZOOM, min(fitted_zoom_, MAX_ZOOM))
        if fitted_zoom_ and fitted_zoom_ != self._zoom:
            self.scale(self._zoom / fitted_zoom_, self._zoom / fitted_zoom_)
        self.zoomChanged.emit(round(self._zoom * 100))
