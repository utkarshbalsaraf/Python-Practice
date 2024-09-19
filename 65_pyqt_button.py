import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 500, 500)
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(200, 200, 100, 50)
        self.button.setStyleSheet("font-size:18px")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(230, 250, 100, 50)
        self.label.setStyleSheet("font-size:18px")

    def on_click(self):
        print("Button Clicked")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label.setText("Bye")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
