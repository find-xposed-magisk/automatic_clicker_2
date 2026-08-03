# 项目名称
Clicker-0.26-Bate（尚未发布）
# 使用说明
主文件为main.py，运行即可。部分功能仍在开发中，可能会出现一些问题。

## 数据目录

Clicker 的可迁移数据统一保存在程序同级的 `data` 文件夹中：

```text
data/
├─ 命令集.db     # 指令、设置、窗口状态、分支、变量和最近打开记录
├─ images/       # 截图和应用自有图片
├─ exports/      # 默认的指令备份目录
├─ logs/         # 默认的操作日志目录
├─ updates/      # 更新包和更新信息
└─ temp/         # 可随时清理的临时文件
```

迁移或备份时复制整个 `data` 文件夹即可。`flat`、`Window` 和图标等目录属于程序静态资源，不是用户数据。用户手动添加的外部资源目录和外部 Excel 文件仍保留原路径引用，不会自动搬移。

核心文件为：main.py、WindowControl/导航窗口功能.py、main_work.py、功能类.py。
## 添加指令的步骤：
1. 在导航页的页面中添加指令的控件（Window/导航窗口.ui）
2. 在导航页的页面中添加指令的处理函数（WindowControl/导航窗口功能.py）
3. 在导航页的treeWidget中添加指令的名称（Window/导航窗口.ui）
4. 在功能类中添加运行功能的函数（功能类.py）
5. 在main_work.py中添加指令的调用函数（main_work.py）
6. 详情请参考代码：添加指令模板.py
## 必须安装的python库
```txt
PyQt5
pyttsx4
pymsgbox
pyautogui
mouse
keyboard
pandas
pillow
openpyxl
requests
system_hotkey
pygments
opencv-python
baidu-aip
chardet
system_hotkey
nuitka
pyinstaller
python-dateutil
psutil
xlrd
```
## 一键安装方法
```txt
pip install PyQt5 pyttsx4 pymsgbox pyautogui mouse keyboard pandas pillow openpyxl requests system_hotkey pygments opencv-python baidu-aip chardet nuitka pyinstaller python-dateutil psutil xlrd
```
# 贡献者
FasterThanLight

邮箱：federalsadler@sohu.com

QQ：2309636438

QQ交流群：308994839    [点击加入](https://qm.qq.com/q/3ih3PE16Mg)
