import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(100, 100, 500, 500)
        self.setWindowIcon(QIcon("pic.jpg"))
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(100, 10, 300, 300)
        label.setStyleSheet(
            "color: #292929;""background-color: #6fdcf7;""font-weight: bold;""font-style: italic;" "text-decoration: underline;")
        # label.setAlignment(Qt.AlignVCenter)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        pixmap = QPixmap("pic.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry((self.width() - label.width()) // 2, (self.height() - label.height()) // 2, label.width(),
                          label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
