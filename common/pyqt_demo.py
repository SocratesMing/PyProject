import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSizePolicy, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 with Matplotlib Example")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)

        self.layout = QVBoxLayout(self.central_widget)

        # 创建 Matplotlib Figure 对象和 Canvas 对象
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(NavigationToolbar(self.canvas, self))
        self.layout.addWidget(self.canvas)

        # 添加一个按钮，用于在图形中添加新点
        self.button = QPushButton('Add Point', self)
        self.button.clicked.connect(self.add_point)
        self.layout.addWidget(self.button)

        # 在 Matplotlib Figure 上绘制一些内容
        self.plot_data()

    def plot_data(self):
        # 获取 Matplotlib 的 Axes 对象
        ax = self.figure.add_subplot(111)

        # 在 Axes 对象上绘制一条简单的曲线
        self.x = [1, 2, 3, 4, 5]
        self.y = [2, 3, 5, 7, 11]
        ax.plot(self.x, self.y, label='Prime Numbers')

        # 设置图形标题和轴标签
        ax.set_title('Prime Numbers Plot')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')

        # 显示图例
        ax.legend()

        # 更新 Matplotlib Canvas
        self.canvas.draw()

    def add_point(self):
        # 在图形中添加新点并更新
        new_x = max(self.x) + 1
        new_y = new_x * 2  # 简单示例，你可以根据需要修改
        self.x.append(new_x)
        self.y.append(new_y)

        # 获取 Matplotlib 的 Axes 对象并更新数据
        ax = self.figure.axes[0]
        ax.plot(new_x, new_y, 'ro', label='New Point')  # 'ro'表示红色圆点
        ax.legend()

        # 更新 Matplotlib Canvas
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
