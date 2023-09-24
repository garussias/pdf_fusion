# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'concatenate_pdf_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os 
from tkinter import filedialog
from tkinter import *
import glob
import  PyPDF2 as pi


class Ui_MainWindow(object):

    def __init__(self):

        self.chemin_script = os.getcwd()
        self.save_path=self.chemin_script
        self.chemin_pdf=self.chemin_script

    
    def select_pdf_folder(self):
        chemin_script = os.getcwd()
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', 1)
        self.chemin_pdf = filedialog.askdirectory(title = "select teh folder with yours pdf files", initialdir = chemin_script)
        self.txtb_pdf_folder.setText(self.chemin_pdf)


    def select_save_folder(self):
        chemin_script = os.getcwd()
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', 1)
        self.save_path = filedialog.askdirectory(title = "select the folder where to save the concatenate pdf ", initialdir = chemin_script)
        self.txtb_save_folder.setText(self.save_path)


    def pdf_fusion(self):

        fout="pdf_fusion.pdf"
        os.chdir(self.chemin_pdf)
        files_list = sorted(glob.glob('*.pdf'),key=os.path.getmtime)
        merger = pi.PdfMerger()
        for pdf in files_list:
            merger.append(open(pdf, 'rb'))

        os.chdir(self.save_path)
        with open("concatenate_pdf.pdf", "wb") as fout:
            merger.write(fout)
        os.chdir(self.chemin_script)
        MainWindow.close()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 289)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.txtb_pdf_folder = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtb_pdf_folder.setGeometry(QtCore.QRect(180, 60, 281, 41))
        self.txtb_pdf_folder.setObjectName("txtb_pdf_folder")
        self.txtb_pdf_folder.setText(self.chemin_pdf)
        

        self.psh_folder_pdf = QtWidgets.QPushButton(self.centralwidget)
        self.psh_folder_pdf.setGeometry(QtCore.QRect(470, 70, 91, 31))
        self.psh_folder_pdf.setObjectName("psh_folder_pdf")
        self.psh_folder_pdf.clicked.connect(self.select_pdf_folder)
        

        self.lb_pdf_folder = QtWidgets.QLabel(self.centralwidget)
        self.lb_pdf_folder.setGeometry(QtCore.QRect(190, 30, 261, 21))
        self.lb_pdf_folder.setObjectName("lb_pdf_folder")
        

        self.txtb_save_folder = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtb_save_folder.setGeometry(QtCore.QRect(180, 130, 281, 41))
        self.txtb_save_folder.setObjectName("txtb_save_folder")
        self.txtb_save_folder.setText(self.chemin_script)

        self.psh_save_folder = QtWidgets.QPushButton(self.centralwidget)
        self.psh_save_folder.setGeometry(QtCore.QRect(470, 130, 91, 31))
        self.psh_save_folder.setObjectName("psh_save_folder")
        self.psh_save_folder.clicked.connect(self.select_save_folder)

        self.lbl_save_folder = QtWidgets.QLabel(self.centralwidget)
        self.lbl_save_folder.setGeometry(QtCore.QRect(190, 110, 261, 21))
        self.lbl_save_folder.setObjectName("lbl_save_folder")

        self.psh_launch_concate = QtWidgets.QPushButton(self.centralwidget)
        self.psh_launch_concate.setGeometry(QtCore.QRect(230, 180, 201, 31))
        self.psh_launch_concate.setObjectName("psh_launch_concate")
        self.psh_launch_concate.clicked.connect(self.pdf_fusion)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.psh_folder_pdf.setText(_translate("MainWindow", "select a folder"))
        self.lb_pdf_folder.setText(_translate("MainWindow", "Folder containing pdf files to concatenate"))
        self.psh_save_folder.setText(_translate("MainWindow", "select a folder"))
        self.lbl_save_folder.setText(_translate("MainWindow", "folder where to save the concatenate file"))
        self.psh_launch_concate.setText(_translate("MainWindow", "concatenate pdf "))


if __name__ == "__main__":
    import sys
    #print(args.text)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

