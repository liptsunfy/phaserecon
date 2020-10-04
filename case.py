# -*- coding: utf-8 -*-
# @Time: 2020/10/4 10:11 
# @Author: lipengtao
# Note:

import sys
from PyQt5.QtWidgets import QWidget, \
    QPushButton, \
    QToolTip, \
    QMessageBox, \
    QApplication, \
    QDesktopWidget, \
    QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, \
    QIcon


# QMainWindow是QWidget的派生类
class CMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # ToolTip设置
        QToolTip.setFont(QFont('华文楷体', 10))

        # statusBar设置
        self.statusBar().showMessage('准备就绪')

        # PushButton设置
        btnQuit = QPushButton('退出', self)
        btnQuit.setToolTip("点击此按钮将退出应用程序！")
        btnQuit.setStatusTip("点击此按钮将退出应用程序！")
        btnQuit.clicked.connect(QCoreApplication.instance().quit)
        btnQuit.resize(btnQuit.sizeHint())
        btnQuit.move(100, 100)

        self.resize(500, 300)
        self.center()
        self.setFont(QFont('华文楷体', 10))
        self.setWindowTitle('PyQt5应用教程（snmplink编著）')
        self.setWindowIcon(QIcon('10.png'))
        self.show()

    def center(self):
        # 得到主窗体的框架信息
        qr = self.frameGeometry()
        # 得到桌面的中心
        cp = QDesktopWidget().availableGeometry().center()
        # 框架的中心与桌面中心对齐
        qr.moveCenter(cp)
        # 自身窗体的左上角与框架的左上角对齐
        self.move(qr.topLeft())

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self,
                                     'PyQt5应用教程（snmplink编著）',
                                     "是否要退出应用程序？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = CMainWindow()
    sys.exit(app.exec_())
