# This Python file uses the following encoding: utf-8
import csv
import os
import sys

# from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
# from PyQt6.QtWidgets import QFileDialog
from ui_form import Ui_Form
import pandas as pd
from hotmap import plot_hotmap


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

        plt = plot_hotmap(csv_path, x_step, y_step)
        plt.show()
        plt.plot()

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
        try:
            # 读取CSV文件
            df = pd.read_csv(csv_path)

            # 校验行和列是否为空
            if df.empty or df.isnull().values.any():
                QMessageBox.critical(self, '错误', '文件包含空行或空列')

            # 校验是否可以将所有元素转换为整数
            if not df.applymap(lambda x: str(x).isdigit()).all().all():
                QMessageBox.critical(self, '错误', '文件包含不能转换为整数的元素')

            QMessageBox.information(self, '信息', 'csv文件合法')


        except Exception as e:
            print(f"错误：{e}")
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
