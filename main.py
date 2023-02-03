import os
from configparser import ConfigParser

config = ConfigParser()
config.read('info/config.ini')
if len(config.get("main","ym")) <= 2:
    print("[Яндекс Музыка] Установка необходимых пакетов.")
    os.system('pip install yandex-music --upgrade')
    os.system('pip install selenium')
    os.system('pip install pypresence')
    os.system('pip install yandex_music')
    os.system('pip install webdriver_manager')
    os.system('pip install keyboard')
    os.system('pip install pywin32')
    os.system('pip install win32co')
    os.system('pip install pyqt6')
    os.system('pip install webbrowser')

import sys
import time
from modules.rpc import MRPC
from modules.yandexmusic import MYAPI
from threading import Thread
from PyQt6 import QtGui
from PyQt6.QtGui import QAction
import webbrowser
from PyQt6.QtCore import QSize, Qt, QRect, QMetaObject, QCoreApplication, QEvent
from PyQt6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QMessageBox
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout
)

class Ui_MainWindow(QMainWindow):
    global ISTOEXITBLYAT
    ISTOEXITBLYAT = False   
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setFixedSize(300, 158)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.setFont(font)
        self.setWindowIcon(QtGui.QIcon("assets/favicon.png"))
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QRect(16, 16, 550, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.AppEnabling)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(16, 62, 269, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ForceUpdate)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(16, 105, 269, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.ForceUpdateToken)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon("assets/favicon.png"))

        lable = QAction("Перейти на гитхаб", self)
        show_action = QAction("Показать", self)
        quit_action = QAction("Выход", self)
        hide_action = QAction("Севрнуть в трей", self)
        lable.triggered.connect(lambda: webbrowser.open('https://github.com/maj0roff/YandexMusicDiscordRPC', new=2))
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)   

        quit_action.triggered.connect(self.fullexit)
        tray_menu = QMenu()
        tray_menu.addAction(lable)
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.show)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Яндекс Музыка RPC"))
        self.checkBox.setText(_translate("MainWindow", "Включить DiscordRPC"))
        self.pushButton.setText(_translate("MainWindow", "Обновить RPC"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить токен Яндекс Музыки"))

    def AppEnabling(self,s):
        if s == 2:
            global thr
            thr = Thread(target=MRPC.callPresence)
            thr.start()
        else:
            thr._delete
            MRPC.Clear()

    def ForceUpdate(self,s):
        if s == 2:
            MRPC.ForceUpdate()
        else:
            MRPC.Clear()

    def ForceUpdateToken(self,s):
        MYAPI.ForceUpdateToken()

    def fullexit():
            global ISTOEXITBLYAT
            ISTOEXITBLYAT = True
            thr._delete()
            QApplication.quit() 

    def closeEvent(self, event):
        if ISTOEXITBLYAT == False:
            event.ignore()
            self.hide()
            self.tray_icon.showMessage("Яндекс Музыка | DiscordRPC", "Приложение свёрнуто в трей",
                                        QSystemTrayIcon.MessageIcon.NoIcon, 500)

def mainGUI():
    app = QApplication(sys.argv)
    
    window = Ui_MainWindow()
    window.show()

    sys.exit(app.exec())
    

if __name__ == '__main__':
    mainGUI()