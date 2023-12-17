import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MatplotlibWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

    def plot_data(self, x, y):
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, label='Data')
        ax.set_title('Matplotlib Widget Plot')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.legend()
        self.canvas.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 with Matplotlib Example")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # 添加一个按钮，点击按钮时显示Matplotlib绘图窗口
        self.button = QPushButton('Show Matplotlib Widget', self)
        self.button.clicked.connect(self.show_matplotlib_widget)
        self.layout.addWidget(self.button)

        # Matplotlib绘图窗口
        self.matplotlib_widget = None

    def show_matplotlib_widget(self):
        # 创建并显示Matplotlib绘图窗口
        self.matplotlib_widget = MatplotlibWidget()
        self.matplotlib_widget.show()

        # 在Matplotlib绘图窗口中绘制数据
        if self.matplotlib_widget:
            x = [1, 2, 3, 4, 5]
            y = [2, 3, 5, 7, 11]
            self.matplotlib_widget.plot_data(x, y)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
