import os
import sys
import tempfile
import unittest
from unittest.mock import patch

from openpyxl import Workbook

import functions
from ini控制 import IniControl


class DataPathTests(unittest.TestCase):
    def test_source_data_is_under_project_folder(self):
        self.assertEqual(functions.DATA_FOLDER, os.path.join(functions.INSTALL_FOLDER, "data"))
        self.assertEqual(functions.CONFIG_PATH, os.path.join(functions.DATA_FOLDER, "config.ini"))
        self.assertEqual(functions.DATABASE_PATH, os.path.join(functions.DATA_FOLDER, "命令集.db"))

    def test_frozen_install_and_resource_folders_are_separate(self):
        executable = os.path.join("D:\\Portable Clicker", "Clicker.exe")
        resource_folder = os.path.join("C:\\Temp", "_MEI123")
        with patch.object(sys, "frozen", True, create=True), \
                patch.object(sys, "executable", executable), \
                patch.object(sys, "_MEIPASS", resource_folder, create=True):
            self.assertEqual(functions.get_install_folder(), os.path.dirname(executable))
            self.assertEqual(functions.get_resource_folder(), resource_folder)

    def test_portable_resource_path_resolves_from_data(self):
        expected = os.path.normpath(os.path.join(functions.DATA_FOLDER, "images"))
        self.assertEqual(IniControl.resolve_resource_path("images"), expected)
        self.assertEqual(IniControl.portable_resource_path(expected), "images")

    def test_excel_import_writes_selected_ini(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "设置"
        sheet.append(["[Config]", None])
        sheet.append(["测试值", "已写入"])

        with tempfile.TemporaryDirectory() as temporary_directory:
            ini_path = os.path.join(temporary_directory, "config.ini")
            ini = IniControl.__new__(IniControl)
            ini.ini_path = ini_path
            ini.excel_to_ini(workbook)

            with open(ini_path, "r", encoding="utf-8") as ini_file:
                self.assertIn("测试值 = 已写入", ini_file.read())


if __name__ == "__main__":
    unittest.main()
