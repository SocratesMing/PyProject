# This Python file uses the following encoding: utf-8
import csv
import os
import subprocess
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from ui_main import Ui_Form
from heatmap import plot_hotmap


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.btn_chose_file.clicked.connect(self.showFileDialog)
        self.ui.btn_check_csv.clicked.connect(self.check_csv)
        self.ui.btn_plot.clicked.connect(self.plot_hotmap)
        self.ui.btn_build_qtfile.clicked.connect(self.saveFile)
        self.ui.btn_res_path.clicked.connect(self.show_directory)
        self.ui.btn_open_res_path.clicked.connect(self.open_res)

        # self.matplotlib_widget = None

    def plot_hotmap(self):
        pass
        csv_path = self.ui.le_csv_file_path.text()
        try:
            spread_plot = self.ui.le_spread_plot.text()
            time_plot = self.ui.le_time_plot.text()
            if spread_plot == '':
                x_step = 50
            else:
                x_step = int(spread_plot)

            if time_plot == '':
                y_step = 60
            else:
                y_step = int(time_plot)
        except Exception as e:
            QMessageBox.critical(self, '错误', '输入格式错误')
        res_path = os.path.abspath(self.ui.le_res_path.text())
        matplotlib_widget = plot_hotmap(csv_path, res_path, x_step, y_step)
        # self.matplotlib_widget.show()
        if matplotlib_widget.plot():
            QMessageBox.information(self, '信息', '处理完毕')
        else:
            QMessageBox.critical(self, '错误', '处理异常')

        # x = [1, 2, 3, 4, 5]
        # y = [2, 3, 5, 7, 11]
        # self.matplotlib_widget.plot_data(x,y)

    def show_directory(self):
        directory = QFileDialog.getExistingDirectory(self, '选择目录')
        if directory:
            self.ui.le_res_path.setText(directory)

    def open_res(self):
        # 打开文件对话框，获取用户选择的目录
        directory = os.path.abspath(self.ui.le_res_path.text())

        if os.path.exists(directory):
            try:
                # 使用explorer命令打开资源管理器并定位到给定路径
                subprocess.run(['explorer', directory], check=True)
            except subprocess.CalledProcessError as e:
                print(f"打开资源管理器时发生错误: {e}")
        else:
            QMessageBox.critical(self, '错误', '路径不存在')

    #
    def showFileDialog(self):
        # 打开文件选择对话框
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("CSV 文件 (*.csv)")
        file_path, _ = file_dialog.getOpenFileName(self, '选择CSV文件')
        if file_path:
            self.ui.le_csv_file_path.setText(file_path)

    def check_csv(self):
        csv_path = self.ui.le_csv_file_path.text()
        ok=True
        try:
            # 读取CSV文件
            with open(csv_path, 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)

                for row_number, row in enumerate(csv_reader, start=1):
                    # 检查是否有空元素
                    if any(element == '' for element in row):
                        QMessageBox.critical(self, '错误', 'csv文件有非空字符，请处理！')
                        return False

                    # 检查是否有非数字类字符
                    for col_number, value in enumerate(row, start=1):
                        if not str(value.strip()).isdigit():
                            print(value)
                            QMessageBox.critical(self, '错误', 'csv文件有非数字类字符，请处理！')
                            return False

            if ok:
                QMessageBox.information(self, '信息', 'csv文件合法')
                return True

        except Exception as e:
            QMessageBox.critical(self, '错误', 'csv文件有非数字类字符，请处理！')
            return False

    def saveFile(self):
        # 打开文件保存对话框
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, '保存策略文件', '', 'Text Files (*.py);;All Files (*)')

        # 如果用户选择了文件路径，保存文本到文件
        if not file_path.endswith('.py'):
            file_path = file_path + ".py"
        print(file_path)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                self.build_qtfile()
                file.write(self.qtfile)
                QMessageBox.information(self, '信息', '策略文件已保存！')
        except Exception as e:
            print(e)

    def build_qtfile(self):
        try:
            with open(r"/创新项目/hotmap.py", 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)
                self.qtfile = content
                print("读取文件完毕")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
# pip install pyinstaller
# pyinstaller --name="热力图" --windowed --onefile -add-data "./icon" main.py
