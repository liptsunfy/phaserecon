# -*- coding:utf-8 -*-
# @Time : 2020/9/30 8:01
# @Author: Li Pengtao
# @Note：

# Form implementation generated from reading ui file 'beta.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
import matplotlib
from FunPhaserecon import unpack, reconstraction
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

matplotlib.use("Qt5Agg")  # 声明使用QT5
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtGui import QImage, QFont

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 520)  # 主界面尺寸
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        '''
        界面左侧指令栏
        Button：原始图像选择，重构，解包裹， 重置
        '''

        # 指令栏边框 左
        self.leftPart = QtWidgets.QGroupBox(MainWindow)
        self.leftPart.setGeometry(QtCore.QRect(10, 80, 150, 390))
        self.leftPart.setObjectName("LeftGroup")

        # 左侧指令栏风格设计
        # self.leftPart.setStyleSheet('''
        #   QPushButton{border:none;color:black;}
        #   QPushButton#left_label{
        #     border:none;
        #     border-bottom:1px solid white;
        #     font-size:18px;
        #     font-weight:700;
        #     font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        #   }
        #   QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        # ''')

        # 按钮“打开文件”设置
        self.btnOpenFile = QtWidgets.QPushButton(self.leftPart)
        self.btnOpenFile.setGeometry(QtCore.QRect(20, 60, 110, 32))  # 位置为相对于Groupbox的坐标
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.btnOpenFile.setStyleSheet("QPushButton{"
                                   "border-color: rgb(0, 0, 0);"
                                   "\nbackground-color: rgb(211,211,211);"
                                   "\ncolor: rgb(0, 0, 0);"
                                   "\nborder-radius: 10px;"
                                   "\npadding: 8;}"
                                   "QPushButton:hover{"
                                   "border-color: rgb(0, 0, 0);"
                                   "\nbackground-color:rgb(255, 255, 255);"
                                   "\ncolor:  rgb(123, 139, 111);"
                                   "\nborder-radius: 10px;"
                                   "\npadding: 8;}")

        # 按钮“重构”设置
        self.btnReconst = QtWidgets.QPushButton(self.leftPart)
        self.btnReconst.setGeometry(QtCore.QRect(20, 120, 110, 32))
        self.btnReconst.setObjectName("btnReconst")
        self.btnReconst.setStyleSheet("QPushButton{"
                                       "border-color: rgb(0, 0, 0);"
                                       "\nbackground-color: rgb(211,211,211);"
                                       "\ncolor: rgb(0, 0, 0);"
                                       "\nborder-radius: 10px;"
                                       "\npadding: 8;}"
                                       "QPushButton:hover{"
                                       "border-color: rgb(0, 0, 0);"
                                       "\nbackground-color:rgb(255, 255, 255);"
                                       "\ncolor:  rgb(123, 139, 111);"
                                       "\nborder-radius: 10px;"
                                       "\npadding: 8;}")

        # 按钮“保存结果”设置
        self.btnSaveResults = QtWidgets.QPushButton(self.leftPart)
        self.btnSaveResults.setGeometry(QtCore.QRect(20, 170, 110, 32))
        self.btnSaveResults.setObjectName("btnSaveResults")
        self.btnSaveResults.setStyleSheet("QPushButton{"
                                       "border-color: rgb(0, 0, 0);"
                                       "\nbackground-color: rgb(211,211,211);"
                                       "\ncolor: rgb(0, 0, 0);"
                                       "\nborder-radius: 10px;"
                                       "\npadding: 8;}"
                                       "QPushButton:hover{"
                                       "border-color: rgb(0, 0, 0);"
                                       "\nbackground-color:rgb(255, 255, 255);"
                                       "\ncolor:  rgb(123, 139, 111);"
                                       "\nborder-radius: 10px;"
                                       "\npadding: 8;}")

        # 按钮“重置”设置
        self.btnClear = QtWidgets.QPushButton(self.leftPart)
        self.btnClear.setGeometry(QtCore.QRect(20, 230, 110, 32))
        self.btnClear.setObjectName("btnClear")
        self.btnClear.setStyleSheet("QPushButton{"
                                       "border-color: rgb(0, 0, 0);"
                                       "\nbackground-color: rgb(211,211,211);"
                                       "\ncolor: rgb(0, 0, 0);"
                                       "\nborder-radius: 10px;"
                                       "\npadding: 8;}"
                                       "QPushButton:hover{"
                                       "border-color: rgb(0, 0, 0);"
                                       "\nbackground-color:rgb(255, 255, 255);"
                                       "\ncolor:  rgb(123, 139, 111);"
                                       "\nborder-radius: 10px;"
                                       "\npadding: 8;}")

        '''
        界面右侧图像显示栏
        '''
        # 右侧显示区域
        self.rightPart = QtWidgets.QGroupBox(MainWindow)  # 右半部分边框
        self.rightPart.setGeometry(QtCore.QRect(180, 80, 780, 390))
        self.rightPart.setObjectName("RightGroup")

        # 原始图像展示区域
        self.labImage = QtWidgets.QLabel(self.centralwidget)
        self.labImage.setGeometry(QtCore.QRect(200, 180, 54, 12))  # 位置
        self.labImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labImage.setObjectName("labImage")

        # 重构结果展示区域
        self.labReconst = QtWidgets.QLabel(self.centralwidget)
        self.labReconst.setGeometry(QtCore.QRect(600, 180, 54, 12))
        self.labReconst.setAlignment(QtCore.Qt.AlignCenter)
        self.labReconst.setObjectName("labReconst")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        # 文本标签
        self.label_sValue = QtWidgets.QLabel(MainWindow)  # s当前取值
        self.label_sValue.setGeometry(QtCore.QRect(600, 400, 100, 50))
        self.label_sValue.setObjectName("label_sValue")

        # 按钮“3维显示”设置
        self.btn3D = QtWidgets.QPushButton(self.rightPart)
        self.btn3D.setGeometry(QtCore.QRect(200, 320, 110, 32))
        self.btn3D.setObjectName("btn3D")
        self.btn3D.setStyleSheet("QPushButton{"
                                 "border-color: rgb(0, 0, 0);"
                                  "\nbackground-color: rgb(211,211,211);"
                                  "\ncolor: rgb(0, 0, 0);"
                                 "\nborder-radius: 10px;"
                                  "\npadding: 8;}"
            "QPushButton:hover{"
                                 "border-color: rgb(0, 0, 0);"
                                 "\nbackground-color:rgb(255, 255, 255);"
                                 "\ncolor:  rgb(123, 139, 111);"
                                 "\nborder-radius: 10px;"
                                 "\npadding: 8;}")


        self.btn3D_1 = QtWidgets.QPushButton(self.rightPart)
        self.btn3D_1.setGeometry(QtCore.QRect(600, 320, 110, 32))
        self.btn3D_1.setObjectName("btn3D_1")
        self.btn3D_1.setStyleSheet("QPushButton{"
                                 "border-color: rgb(0, 0, 0);"
                                 "\nbackground-color: rgb(211,211,211);"
                                 "\ncolor: rgb(0, 0, 0);"
                                 "\nborder-radius: 10px;"
                                 "\npadding: 8;}"
                                 "QPushButton:hover{"
                                 "border-color: rgb(0, 0, 0);"
                                 "\nbackground-color:rgb(255, 255, 255);"
                                 "\ncolor:  rgb(123, 139, 111);"
                                 "\nborder-radius: 10px;"
                                 "\npadding: 8;}")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "相位重构 v1.0"))
        MainWindow.setWindowIcon(QtGui.QIcon('MyDIP.ico'))  # 窗口图标

        # 窗口上方菜单栏
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))

        # 分栏标签
        self.leftPart.setTitle(_translate("MatrixWin", "控制面板"))
        self.leftPart.setFont(QFont("Roman times", 8, QFont.Bold))  # 调整字体属性
        self.rightPart.setTitle(_translate("MatrixWin", "结果显示"))
        self.rightPart.setFont(QFont("Roman times", 8, QFont.Bold))  # 调整字体属性

        # 原始图像展示区域
        self.labImage.setText(_translate("MainWindow", "原始图像"))
        self.labImage.setFixedSize(350, 240)  # 尺寸设置
        self.labImage.move(200, 100)
        self.labImage.setStyleSheet("QLabel{background:white;}")

        # 重构结果展示区域
        self.labReconst.setText(_translate("MainWindow", "重构结果"))
        self.labReconst.move(580, 100)
        self.labReconst.setFixedSize(350, 240)
        self.labReconst.setStyleSheet("QLabel{background:white;}")

        # 窗口功能按钮
        self.btnOpenFile.setText(_translate("MainWindow", "选择图像"))
        self.btnClear.setText(_translate("MainWindow", "重置"))
        self.btnReconst.setText(_translate("MainWindow", "执行重构"))
        self.btnSaveResults.setText(_translate("MainWindow", "保存重构结果"))
        self.btn3D.setText((_translate("MainWindow","3维显示")))
        self.btn3D_1.setText((_translate("MainWindow", "3维显示")))


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)

        layout = QVBoxLayout()

        '''
        ## 功能按钮 链接事件
        ## “执行解包裹”： 当点击“执行解包裹”按钮时，弹出子窗口，输入S取值，并显示解包裹计算结果
        '''
        self.btnOpenFile.clicked.connect(self.openFile)  # 打开文件
        self.btnReconst.clicked.connect(self.inputS)  # 点击开始重构计算
        self.btnSaveResults.clicked.connect(self.saveReconst)  # 保存重构结果
        self.btnClear.clicked.connect(self.clearAll)  # 重置选择文件
        self.btn3D.clicked.connect(self.tripD_display)  # 解包裹结果3维显示
        self.btn3D_1.clicked.connect(self.tripD_display1)  # 重构结果3维显示


    '''
    软件功能
    '''

    def openFile(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.bmp;;All Files(*)")
        oriImg = QtGui.QPixmap(imgName).scaled(self.labImage.width(), self.labImage.height())

        global inputImg_path  # 设置一个全局变量用来传递图像绝对路径
        inputImg_path = imgName

        self.labImage.setPixmap(oriImg)  # 显示打开的图像

    # 输入S值
    def inputS(self, event):  # 输入：整数
        try:
            inputImg_path
        except:
            self.showMessageBox()  # 警告！
        else:
            # 后面四个数字的作用依次是 初始值 最小值 最大值 步幅
            value, ok = QInputDialog.getInt(self, "执行重构", "请输入s值\n\n请输入整数(点击ok，即可执行重构):", 37, 0, 10000, 1)

            global input_s
            input_s = value  # s值 全局变量传递给重构函数

            if ok:
                self.reConst()
                self.label_sValue.setText("当前s取值：\n   s = {}".format(input_s))  # 显示当前S取值
                self.label_sValue.setFont(QFont("Roman times", 8, QFont.Bold))  # 调整字体属性


    # 重构
    def reConst(self):
        upResults = unpack(inputImg_path)  # 第一步图像解包裹结果

        global valur_for_display
        valur_for_display = upResults

        n_row = upResults.shape[0]
        n_col = upResults.shape[1]

        data = np.array(list(upResults), dtype='float64')
        input_for_recon = data.reshape(n_row, n_col)

        # 重构结果
        value_results = reconstraction(input_for_recon, s=input_s, d=4)

        global value_for_3Ddisplay1
        value_for_3Ddisplay1 = value_results

        value_results = value_results.astype(np.uint8)  # 更改数据类型

        # 将array 转换成QImage
        im = QImage(value_results.data, value_results.shape[1], value_results.shape[0], value_results.shape[1],
                    QImage.Format_Indexed8)
        reconstImg = QtGui.QPixmap(im).scaled(n_col, n_row)

        global recontResults
        recontResults = value_results  # 将结果传递给解包裹函数

        self.labReconst.setPixmap(reconstImg)  # 显示输出的图像
        self.labReconst.setScaledContents(True)  # 图片自适应label大小


    def tripD_display(self):
        try:
            valur_for_display
        except:
            self.showMessageBox()  # 警告！
        else:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            size = valur_for_display.shape
            Y = np.arange(0, size[0], 1)
            X = np.arange(0, size[1], 1)

            X, Y = np.meshgrid(X, Y)

            surf = ax.plot_surface(X, Y, valur_for_display, cmap=cm.coolwarm)
            fig.colorbar(surf, shrink=0.5, aspect=5)

            plt.show()

    def tripD_display1(self):
        try:
            value_for_3Ddisplay1
        except:
            self.showMessageBox()  # 警告！
        else:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            size = value_for_3Ddisplay1.shape
            Y = np.arange(0, size[0], 1)
            X = np.arange(0, size[1], 1)

            X, Y = np.meshgrid(X, Y)

            surf = ax.plot_surface(X, Y, value_for_3Ddisplay1, cmap=cm.coolwarm)
            fig.colorbar(surf, shrink=0.5, aspect=5)

            plt.show()


    # 保存重构结果
    def saveReconst(self):
        try:
            recontResults
        except:
            self.showMessageBox_1()  # 警告！
        else:
            screen = QApplication.primaryScreen()
            pix = screen.grabWindow(self.labReconst.winId())
            reImg, type = QFileDialog.getSaveFileName(self.centralwidget, "保存图片", "", "*.bmp;;All Files(*)")
            pix.save(reImg)


    def clearAll(self):
        try:
            inputImg_path
        except:
            self.showMessageBox_2()  # 警告！
        else:
            self.labImage.clear()
            self.labImage.setText("请重新选择待处理图像")
            self.labReconst.setText("重构结果")
            self.label_sValue.clear()

            # 清除全局变量  inputImg_path，input_s，valur_for_display，value_for_3Ddisplay1，recontResults




    # 警告！
    def showMessageBox(self):
        res_0 = QMessageBox.warning(self, "警告", "错误操作！请先执行上一步骤！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    # 警告！
    def showMessageBox_1(self):
        res_1 = QMessageBox.warning(self, "警告", "没有可以保存的图片！请按顺序执行！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    # 警告！
    def showMessageBox_2(self):
        res_2 = QMessageBox.warning(self, "警告", "当前无需重置！", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
