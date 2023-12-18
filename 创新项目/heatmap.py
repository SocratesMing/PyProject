import csv
import os

import matplotlib.pyplot as plt



class plot_hotmap:

    def __init__(self, path_csv, res_path=None, x_step=50, y_step=60):
        super().__init__()

        self.path = os.path.abspath(path_csv)
        self.res_path = res_path
        self.x_step = x_step
        self.y_step = y_step // 60

        # 创建 Matplotlib Figure 对象和 Canvas 对象
        # self.setWindowTitle("结果绘图")
        # self.figure = Figure()
        # self.canvas = FigureCanvas(self.figure)
        # self.layout = QVBoxLayout(self)
        # self.layout.addWidget(self.canvas)

        # 创建 Matplotlib NavigationToolbar

    def plot(self):
        # 创建一个示例的二维数组
        # data = np.random.rand(5, 5)  # 5x5的随机数据，可以替换为您的实际数据
        try:
            with open(self.path, 'r', newline='') as csv_file:
                data = []
                csv_reader = csv.reader(csv_file)
                for row_number, row in enumerate(csv_reader, start=1):
                    cow = []
                    # 检查是否有空元素
                    # 检查是否有非数字类字符
                    for col_number, value in enumerate(row, start=1):
                        cow.append(int(value.strip()))
                    data.append(cow)

                # 创建热力图
                plt.figure(figsize=(8, 6))
                heatmap = plt.imshow(data, cmap='Reds', aspect='auto')
                # 添加颜色栏
                plt.colorbar(heatmap)

                # 设置中文字体属性
                plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换为您的中文字体名称
                plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
                # 显示热力值
                print(data)

                for row in range(len(data)):
                    for col in range(len(data[0])):
                        plt.annotate(f'{data[row][col]}', (col, row), color='black', fontsize=12,
                                     ha='center', va='center')

                # 设置横轴和纵轴标签
                plt.ylabel('时间/Time(Hour)')
                plt.xlabel('价差/SPread')
                rows = len(data)
                cols = len(data[0])

                # 设置刻标和标签
                y_tick_positions = range(0, rows, 1)
                y_tick_labels = range(0, rows * self.y_step, self.y_step)
                plt.yticks(y_tick_positions, y_tick_labels)
                # ax.set_yticklabels(y_tick_labels)
                # ax.yaxis.set_major_locator(FixedLocator(y_tick_positions))

                x_tick_positions = range(0, cols, 1)
                x_tick_labels = range(0, cols * self.x_step, self.x_step)
                plt.xticks(x_tick_positions, x_tick_labels)
                # 添加标题
                plt.title('价差时间热力图')
                print("开始保存文件")
                print(self.res_path)
                print(os.path.dirname(self.path))
                if self.res_path is not None:
                    path = os.path.join(self.res_path, "heatmap.png")
                else:
                    path = os.path.join(os.path.dirname(self.path), "heatmap.png")
                print(path)
                plt.savefig(path)
                return True
        except Exception as e:
            print("保存文件异常", e)
            return False

        #
        # # 显示图表
        # # plt.show()
        # # self.canvas.draw()
        # plt.legend()

        ##########################
        # ax = self.figure.add_subplot(111)
        #
        # heatmap = ax.imshow(data, cmap='Reds', aspect='auto')
        # rows, cols = data.shape
        #
        # # 添加颜色栏
        # self.figure.colorbar(heatmap)
        #
        # # 显示热力值
        # for i in range(rows):
        #     for j in range(cols):
        #         ax.text(j, i, str(data[i, j]), color='black', fontsize=12,
        #                 ha='center', va='center')
        #
        # # Customize x-axis and y-axis ticks
        # y_tick_positions = np.arange(0, data.shape[0], 1)  # 显示y轴的刻标
        # y_tick_labels = np.arange(0, data.shape[0] * self.y_step, self.y_step)  ## 显示y轴的刻标以及对应的标签
        # #
        # plt.yticks(y_tick_positions, labels=y_tick_labels)
        # ax.yaxis.set_major_locator(FixedLocator(y_tick_positions))
        #
        # x_tick_positions = np.arange(0, data.shape[1], 1)  # 显示x轴的刻标
        # x_tick_labels = np.arange(0, data.shape[1] * self.x_step, self.x_step)  ## 显示x轴的刻标以及对应的标签
        # plt.xticks(x_tick_positions, labels=x_tick_labels)
        # ax.xaxis.set_major_locator(FixedLocator(x_tick_positions))
        #
        # # 设置中文字体
        # font = FontProperties(fname='icon/msyh.ttc', size=10)  # 替换为微软雅黑字体文件路径
        # ax.set_xticklabels(x_tick_labels, fontproperties=font)
        # ax.set_yticklabels(y_tick_labels, fontproperties=font)
        # ax.set_xlabel('价差/SPread', fontproperties=font)
        # ax.set_ylabel('时间/Time(Hour)', fontproperties=font)
        # ax.set_title('价差时间热力图', fontproperties=font)
        #
        # # 显示图表
        # self.canvas.draw()

        # self.canvas.draw()

    # def plot_data(self, x, y):
    #     ax = self.figure.add_subplot(111)
    #     ax.plot(x, y, label='Data')
    #     ax.set_title('Matplotlib Widget Plot')
    #     ax.set_xlabel('X-axis')
    #     ax.set_ylabel('Y-axis')
    #     ax.legend()
    #     self.canvas.draw()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    window = plot_hotmap("D:\Code\PyProject\创新项目\data.csv")
    # window.show()
    window.plot()
    # sys.exit(app.exec())
