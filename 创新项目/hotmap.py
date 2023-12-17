import sys

import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import FixedLocator


class plot_hotmap(QWidget):

    def __init__(self, path, x_step=50, y_step=60):
        super().__init__()

        self.path = path
        self.x_step =  x_step
        self.y_step = y_step/60


        # 创建 Matplotlib Figure 对象和 Canvas 对象
        self.setWindowTitle("结果绘图")
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QVBoxLayout(self)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)

        # 创建 Matplotlib NavigationToolbar


    def plot(self):
        # 创建一个示例的二维数组
        # data = np.random.rand(5, 5)  # 5x5的随机数据，可以替换为您的实际数据
        data = np.genfromtxt(self.path, delimiter=',', dtype=int)
        # 创建热力图
        # plt.figure(figsize=(8, 6))
        # heatmap = plt.imshow(data, cmap='Reds', aspect='auto')
        # rows, cols = data.shape
        # print(rows, cols)
        # # 添加颜色栏
        # plt.colorbar(heatmap)
        #
        # # 设置中文字体属性
        # plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换为您的中文字体名称
        # plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        # # 显示热力值
        # for i in range(data.shape[0]):
        #     for j in range(data.shape[1]):
        #         plt.annotate(f'{data[i, j]}', (j, i), color='black', fontsize=12,
        #                      ha='center', va='center')

        #
        # # 设置横轴和纵轴标签
        # plt.ylabel('时间/Time(Hour)')
        # plt.xlabel('价差/SPread')
        # # plt.xticks(np.arange(0, cols * self.x_step + 1, self.x_step))
        # # plt.yticks(np.arange(0, rows * self.y_step + 1, 1))
        # # print(np.arange(0, cols * self.x_step + 1, self.x_step))
        # # print(np.arange(0, cols, self.y_step))
        #
        # # 添加标题
        # plt.title('价差时间热力图')
        #
        # # 显示图表
        # # plt.show()
        # # self.canvas.draw()
        # plt.legend()

        ##########################
        ax = self.figure.add_subplot(111)

        heatmap = ax.imshow(data, cmap='Reds', aspect='auto')
        rows, cols = data.shape

        # 添加颜色栏
        self.figure.colorbar(heatmap)

        # 显示热力值
        for i in range(rows):
            for j in range(cols):
                ax.text(j, i, str(data[i, j]), color='black', fontsize=12,
                        ha='center', va='center')

        # Customize x-axis and y-axis ticks
        y_tick_positions = np.arange(0, data.shape[0], 1)  # 显示y轴的刻标
        y_tick_labels = np.arange(0, data.shape[0] * self.y_step, self.y_step)  ## 显示y轴的刻标以及对应的标签
        #
        plt.yticks(y_tick_positions, labels=y_tick_labels)
        ax.yaxis.set_major_locator(FixedLocator(y_tick_positions))

        x_tick_positions = np.arange(0, data.shape[1], 1)  # 显示x轴的刻标
        x_tick_labels = np.arange(0, data.shape[1] * self.x_step, self.x_step)  ## 显示x轴的刻标以及对应的标签
        plt.xticks(x_tick_positions, labels=x_tick_labels)
        ax.xaxis.set_major_locator(FixedLocator(x_tick_positions))

        # 设置中文字体
        font = FontProperties(fname='icon/msyh.ttc', size=10)  # 替换为微软雅黑字体文件路径
        ax.set_xticklabels(x_tick_labels, fontproperties=font)
        ax.set_yticklabels(y_tick_labels, fontproperties=font)
        ax.set_xlabel('价差/SPread', fontproperties=font)
        ax.set_ylabel('时间/Time(Hour)', fontproperties=font)
        ax.set_title('价差时间热力图', fontproperties=font)

        # 显示图表
        self.canvas.draw()

        # self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = plot_hotmap("data.csv")
    window.show()
    window.plot()
    sys.exit(app.exec())