from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QSizeGrip
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
import os
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Expense Tracker")

        toolbar = QToolBar('Tool Bar')
        toolbar.setIconSize(QSize(64,64))
        self.addToolBar(toolbar)
        
        quitaction = toolbar.addAction("Quit")
        quitaction.triggered.connect(self.quit_app)
        
        action1 = QAction('Some Action', self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.action1triggered)
        toolbar.addAction(action1)
        
        clearTerminal = QAction(QIcon("start.png"), 'Clear Terminal', self)
        clearTerminal.setStatusTip("Status message for some action")
        clearTerminal.triggered.connect(self.clearTerminal)
        #clearTerminal.setCheckable(True)
        toolbar.addAction(clearTerminal)
        
    def quit_app(self):
        self.app.quit()
        
        
    def action1triggered(self):
        print('Action1 Triggered')
        
    def clearTerminal(self):
        os.system("cls")
        print('Terminal Cleared')