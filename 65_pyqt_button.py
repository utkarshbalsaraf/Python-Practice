import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QCheckBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 300, 500, 600)
        # Button
        self.button = QPushButton("Click me!", self)
        self.label1 = QLabel("Hello", self)

        # Checkbox
        self.checkbox = QCheckBox("Checked ?", self)
        self.label2 = QLabel("Not Checked", self)

        # Radio Buttons
        self.label3 = QLabel("Choose Card", self)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master Card", self)
        self.radio3 = QRadioButton("RuPay", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.btn_grp1 = QButtonGroup(self)
        self.btn_grp2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        # Button
        self.button.setGeometry(200, 200, 100, 50)
        self.button.setStyleSheet("font-size:18px")
        self.button.clicked.connect(self.on_click)
        self.label1.setGeometry(230, 250, 100, 50)
        self.label1.setStyleSheet("font-size:18px")

        # Checkbox
        self.checkbox.setGeometry(200, 90, 120, 100)
        self.checkbox.setStyleSheet("font-size:18px")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.is_checked)
        self.label2.setGeometry(230, 140, 100, 50)
        self.label2.setStyleSheet("color:red;")

        # Radio Buttons
        self.label3.setGeometry(220, 300, 100, 50)
        self.label3.setStyleSheet("font-size:18px")
        self.radio1.setGeometry(200, 305, 120, 100)
        self.radio2.setGeometry(200, 330, 120, 100)
        self.radio3.setGeometry(200, 355, 120, 100)
        self.radio4.setGeometry(200, 390, 120, 100)
        self.radio5.setGeometry(200, 415, 120, 100)
        self.setStyleSheet("QRadioButton{" "font-size : 15px;""}")
        self.btn_grp1.addButton(self.radio1)
        self.btn_grp1.addButton(self.radio2)
        self.btn_grp1.addButton(self.radio3)
        self.btn_grp2.addButton(self.radio4)
        self.btn_grp2.addButton(self.radio5)



    def on_click(self):
        print("Button Clicked")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label1.setText("Bye")

    def is_checked(self, state):
        if state == Qt.Checked:
            self.label2.setText("Checked")
            self.label2.setStyleSheet("color:green;")
        else:
            self.label2.setText("Not Checked")
            self.label2.setStyleSheet("color:red;")

    def selection(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
