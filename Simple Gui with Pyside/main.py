import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Boobies')
        button1 = QPushButton("Test Button")
        button1.clicked.connect(self.button1_clicked)
        
        button2 = QPushButton("Test Button")
        button2.clicked.connect(self.button2_clicked)
        
        button_layoutV = QVBoxLayout()
        button_layoutV.addWidget(button1)
        button_layoutV.addWidget(button2)

        self.setLayout(button_layoutV)

    def button1_clicked(self):
        print("hello button 1")


    def button2_clicked(self):
        print("hello button 2")
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()