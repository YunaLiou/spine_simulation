# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog


import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk.util.numpy_support import numpy_to_vtk, vtk_to_numpy
import torch
import numpy as np
import cv2
import torch.nn.functional as F




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 1005)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saveBTN = QtWidgets.QPushButton(self.centralwidget)
        self.saveBTN.setGeometry(QtCore.QRect(580, 940, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.saveBTN.setFont(font)
        self.saveBTN.setObjectName("saveBTN")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 840, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 870, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 900, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.updateBTN = QtWidgets.QPushButton(self.centralwidget)
        self.updateBTN.setGeometry(QtCore.QRect(290, 940, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.updateBTN.setFont(font)
        self.updateBTN.setObjectName("updateBTN")
        self.label_fluro = QtWidgets.QLabel(self.centralwidget)
        self.label_fluro.setGeometry(QtCore.QRect(440, 70, 450, 450))
        self.label_fluro.setText("")
        self.label_fluro.setScaledContents(True)
        self.label_fluro.setObjectName("label_fluro")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1130, -20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(660, 540, 251, 241))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 540, 251, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_1 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_1.setContentsMargins(0, 0, 0, 0)
        self.formLayout_1.setObjectName("formLayout_1")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(390, 540, 251, 241))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(40, 40, 351, 331))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_all = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_all.setContentsMargins(0, 0, 0, 0)
        self.formLayout_all.setObjectName("formLayout_all")
        self.rotY_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.rotY_3.setGeometry(QtCore.QRect(740, 870, 91, 22))
        self.rotY_3.setObjectName("rotY_3")
        self.rotX_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.rotX_1.setGeometry(QtCore.QRect(180, 840, 91, 22))
        self.rotX_1.setObjectName("rotX_1")
        self.rotY_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.rotY_2.setGeometry(QtCore.QRect(470, 870, 91, 22))
        self.rotY_2.setObjectName("rotY_2")
        self.rotZ_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.rotZ_2.setGeometry(QtCore.QRect(470, 900, 91, 22))
        self.rotZ_2.setObjectName("rotZ_2")
        self.rotY_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.rotY_1.setGeometry(QtCore.QRect(180, 870, 91, 22))
        self.rotY_1.setObjectName("rotY_1")
        self.rotX_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.rotX_2.setGeometry(QtCore.QRect(470, 840, 91, 22))
        self.rotX_2.setObjectName("rotX_2")
        self.rotX_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.rotX_3.setGeometry(QtCore.QRect(740, 840, 91, 22))
        self.rotX_3.setObjectName("rotX_3")
        self.rotZ_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.rotZ_1.setGeometry(QtCore.QRect(180, 900, 91, 22))
        self.rotZ_1.setObjectName("rotZ_1")
        self.rotZ_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.rotZ_3.setGeometry(QtCore.QRect(740, 900, 91, 22))
        self.rotZ_3.setObjectName("rotZ_3")
        self.TransX_slider = QtWidgets.QSlider(self.centralwidget)
        self.TransX_slider.setGeometry(QtCore.QRect(140, 380, 241, 16))
        self.TransX_slider.setMinimum(-180)
        self.TransX_slider.setMaximum(180)
        self.TransX_slider.setOrientation(QtCore.Qt.Horizontal)
        self.TransX_slider.setObjectName("TransX_slider")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 400, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.TransZ_slider = QtWidgets.QSlider(self.centralwidget)
        self.TransZ_slider.setGeometry(QtCore.QRect(140, 420, 241, 16))
        self.TransZ_slider.setMinimum(-180)
        self.TransZ_slider.setMaximum(180)
        self.TransZ_slider.setOrientation(QtCore.Qt.Horizontal)
        self.TransZ_slider.setObjectName("TransZ_slider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 380, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.TransZ_label = QtWidgets.QLabel(self.centralwidget)
        self.TransZ_label.setGeometry(QtCore.QRect(100, 410, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.TransZ_label.setFont(font)
        self.TransZ_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TransZ_label.setObjectName("TransZ_label")
        self.TransY_label = QtWidgets.QLabel(self.centralwidget)
        self.TransY_label.setGeometry(QtCore.QRect(100, 390, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.TransY_label.setFont(font)
        self.TransY_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TransY_label.setObjectName("TransY_label")
        self.TransY_slider = QtWidgets.QSlider(self.centralwidget)
        self.TransY_slider.setGeometry(QtCore.QRect(140, 400, 241, 16))
        self.TransY_slider.setMinimum(-180)
        self.TransY_slider.setMaximum(180)
        self.TransY_slider.setOrientation(QtCore.Qt.Horizontal)
        self.TransY_slider.setObjectName("TransY_slider")
        self.TransX_label = QtWidgets.QLabel(self.centralwidget)
        self.TransX_label.setGeometry(QtCore.QRect(100, 380, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.TransX_label.setFont(font)
        self.TransX_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TransX_label.setObjectName("TransX_label")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 420, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.RotX_label = QtWidgets.QLabel(self.centralwidget)
        self.RotX_label.setGeometry(QtCore.QRect(100, 430, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.RotX_label.setFont(font)
        self.RotX_label.setAlignment(QtCore.Qt.AlignCenter)
        self.RotX_label.setObjectName("RotX_label")
        self.RotX_slider = QtWidgets.QSlider(self.centralwidget)
        self.RotX_slider.setGeometry(QtCore.QRect(140, 440, 241, 16))
        self.RotX_slider.setMinimum(-180)
        self.RotX_slider.setMaximum(180)
        self.RotX_slider.setOrientation(QtCore.Qt.Horizontal)
        self.RotX_slider.setObjectName("RotX_slider")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 480, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.RotY_slider = QtWidgets.QSlider(self.centralwidget)
        self.RotY_slider.setGeometry(QtCore.QRect(140, 460, 241, 16))
        self.RotY_slider.setMinimum(-180)
        self.RotY_slider.setMaximum(180)
        self.RotY_slider.setOrientation(QtCore.Qt.Horizontal)
        self.RotY_slider.setObjectName("RotY_slider")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 440, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.RotY_label = QtWidgets.QLabel(self.centralwidget)
        self.RotY_label.setGeometry(QtCore.QRect(100, 450, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.RotY_label.setFont(font)
        self.RotY_label.setAlignment(QtCore.Qt.AlignCenter)
        self.RotY_label.setObjectName("RotY_label")
        self.RotZ_slider = QtWidgets.QSlider(self.centralwidget)
        self.RotZ_slider.setGeometry(QtCore.QRect(140, 480, 241, 16))
        self.RotZ_slider.setMinimum(-180)
        self.RotZ_slider.setMaximum(180)
        self.RotZ_slider.setOrientation(QtCore.Qt.Horizontal)
        self.RotZ_slider.setObjectName("RotZ_slider")
        self.RotsZ_label = QtWidgets.QLabel(self.centralwidget)
        self.RotsZ_label.setGeometry(QtCore.QRect(100, 470, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.RotsZ_label.setFont(font)
        self.RotsZ_label.setAlignment(QtCore.Qt.AlignCenter)
        self.RotsZ_label.setObjectName("RotsZ_label")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 460, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(590, 20, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.UpdateAllBTN = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateAllBTN.setGeometry(QtCore.QRect(180, 500, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.UpdateAllBTN.setFont(font)
        self.UpdateAllBTN.setObjectName("UpdateAllBTN")
        self.Load1BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Load1BTN.setGeometry(QtCore.QRect(180, 790, 111, 23))
        self.Load1BTN.setObjectName("Load1BTN")
        self.Load2BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Load2BTN.setGeometry(QtCore.QRect(460, 790, 111, 23))
        self.Load2BTN.setObjectName("Load2BTN")
        self.Load3BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Load3BTN.setGeometry(QtCore.QRect(740, 790, 111, 23))
        self.Load3BTN.setObjectName("Load3BTN")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.frame_1 = QtWidgets.QFrame()
        self.vtkWidget_1 = QVTKRenderWindowInteractor(self.frame_1)
        self.formLayout_1.addWidget(self.vtkWidget_1)
        self.ren_1 = vtk.vtkRenderer()
        self.vtkWidget_1.GetRenderWindow().AddRenderer(self.ren_1)
        self.iren_1 = self.vtkWidget_1.GetRenderWindow().GetInteractor()

        self.frame_2 = QtWidgets.QFrame()
        self.vtkWidget_2 = QVTKRenderWindowInteractor(self.frame_2)
        self.formLayout_2.addWidget(self.vtkWidget_2)
        self.ren_2 = vtk.vtkRenderer()
        self.vtkWidget_2.GetRenderWindow().AddRenderer(self.ren_2)
        self.iren_2 = self.vtkWidget_2.GetRenderWindow().GetInteractor()

        self.frame_3 = QtWidgets.QFrame()
        self.vtkWidget_3 = QVTKRenderWindowInteractor(self.frame_3)
        self.formLayout_3.addWidget(self.vtkWidget_3)
        self.ren_3 = vtk.vtkRenderer()
        self.vtkWidget_3.GetRenderWindow().AddRenderer(self.ren_3)
        self.iren_3 = self.vtkWidget_3.GetRenderWindow().GetInteractor()


        self.frame_all = QtWidgets.QFrame()
        self.vtkWidget_all = QVTKRenderWindowInteractor(self.frame_all)
        self.formLayout_all.addWidget(self.vtkWidget_all)
        self.ren_all = vtk.vtkRenderer()
        self.vtkWidget_all.GetRenderWindow().AddRenderer(self.ren_all)
        self.iren_all = self.vtkWidget_all.GetRenderWindow().GetInteractor()

        self.bone_1 = np.zeros((180, 180, 180))
        self.bone_2 = np.zeros((180, 180, 180))
        self.bone_3 = np.zeros((180, 180, 180))



        self.Load1BTN.clicked.connect(self.load1bone)
        self.Load2BTN.clicked.connect(self.load2bone)
        self.Load3BTN.clicked.connect(self.load3bone)
        self.updateBTN.clicked.connect(self.update)



    def load1bone(self):
        self.filefolder_1 = QFileDialog.getExistingDirectory(None, "選取資料夾")
        if self.filefolder_1 == "":
            print("\n取消選擇")
            return

        self.ren_1.RemoveAllViewProps()

        self.PNG_Reader_1 = vtk.vtkPNGReader()
        self.PNG_Reader_1.SetNumberOfScalarComponents(1)
        self.PNG_Reader_1.SetFileDimensionality(3)
        self.PNG_Reader_1.SetDataExtent(0, 180, 0, 180, 0, 179)
        self.PNG_Reader_1.SetFilePrefix(self.filefolder_1+'/')
        self.PNG_Reader_1.SetFilePattern("%s%d.png")
        self.PNG_Reader_1.Update()
        self.PNG_Reader_1.SetDataByteOrderToLittleEndian()

        self.PNG_contour_1 = vtk.vtkDiscreteMarchingCubes()
        self.PNG_contour_1.SetInputConnection(self.PNG_Reader_1.GetOutputPort())
        self.PNG_contour_1.ComputeNormalsOn()
        self.PNG_contour_1.SetValue(0, 255)

        self.PNG_sinc_1 = vtk.vtkWindowedSincPolyDataFilter()
        self.PNG_sinc_1.SetInputConnection(self.PNG_contour_1.GetOutputPort())
        self.PNG_sinc_1.SetNumberOfIterations(50)
        self.PNG_sinc_1.SetPassBand(0.003)

        PNG_mapper_1 = vtk.vtkPolyDataMapper()
        PNG_mapper_1.SetInputConnection(self.PNG_sinc_1.GetOutputPort())
        PNG_mapper_1.ScalarVisibilityOff()

        PNG_actor_1 = vtk.vtkActor()
        PNG_actor_1.SetMapper(PNG_mapper_1)

        PNG_renderer_1 = vtk.vtkRenderer()
        PNG_renderer_1.SetBackground([0.1, 0.1, 0.1])
        PNG_renderer_1.AddActor(PNG_actor_1)

        cameraR_1 = vtk.vtkCamera()
        cameraR_1.SetPosition(0, 1000, 0)
        cameraR_1.SetFocalPoint(0, 0, 0)
        cameraR_1.SetViewUp(0, 0, -1.0)

        self.ren_1.SetActiveCamera(cameraR_1)
        self.ren_1.AddActor(PNG_actor_1)
        self.ren_1.ResetCamera()
        self.iren_1.Initialize()
        self.iren_1.Start()

    def load2bone(self):
        self.filefolder_2 = QFileDialog.getExistingDirectory(None, "選取資料夾")
        if self.filefolder_2 == "":
            print("\n取消選擇")
            return

        self.ren_2.RemoveAllViewProps()

        self.PNG_Reader_2 = vtk.vtkPNGReader()
        self.PNG_Reader_2.SetNumberOfScalarComponents(1)
        self.PNG_Reader_2.SetFileDimensionality(3)
        self.PNG_Reader_2.SetDataExtent(0, 180, 0, 180, 0, 179)
        self.PNG_Reader_2.SetFilePrefix(self.filefolder_2+'/')
        self.PNG_Reader_2.SetFilePattern("%s%d.png")
        self.PNG_Reader_2.Update()
        self.PNG_Reader_2.SetDataByteOrderToLittleEndian()

        self.PNG_contour_2 = vtk.vtkDiscreteMarchingCubes()
        self.PNG_contour_2.SetInputConnection(self.PNG_Reader_2.GetOutputPort())
        self.PNG_contour_2.ComputeNormalsOn()
        self.PNG_contour_2.SetValue(0, 255)

        self.PNG_sinc_2 = vtk.vtkWindowedSincPolyDataFilter()
        self.PNG_sinc_2.SetInputConnection(self.PNG_contour_2.GetOutputPort())
        self.PNG_sinc_2.SetNumberOfIterations(50)
        self.PNG_sinc_2.SetPassBand(0.003)

        PNG_mapper_2 = vtk.vtkPolyDataMapper()
        PNG_mapper_2.SetInputConnection(self.PNG_sinc_2.GetOutputPort())
        PNG_mapper_2.ScalarVisibilityOff()

        PNG_actor_2 = vtk.vtkActor()
        PNG_actor_2.SetMapper(PNG_mapper_2)

        PNG_renderer_2 = vtk.vtkRenderer()
        PNG_renderer_2.SetBackground([0.1, 0.1, 0.1])
        PNG_renderer_2.AddActor(PNG_actor_2)

        cameraR_2 = vtk.vtkCamera()
        cameraR_2.SetPosition(0, 1000, 0)
        cameraR_2.SetFocalPoint(0, 0, 0)
        cameraR_2.SetViewUp(0, 0, -1.0)

        self.ren_2.SetActiveCamera(cameraR_2)
        self.ren_2.AddActor(PNG_actor_2)
        self.ren_2.ResetCamera()
        self.iren_2.Initialize()
        self.iren_2.Start()

    def load3bone(self):
        self.filefolder_3 = QFileDialog.getExistingDirectory(None, "選取資料夾")
        if self.filefolder_3 == "":
            print("\n取消選擇")
            return

        self.ren_3.RemoveAllViewProps()

        self.PNG_Reader_3 = vtk.vtkPNGReader()
        self.PNG_Reader_3.SetNumberOfScalarComponents(1)
        self.PNG_Reader_3.SetFileDimensionality(3)
        self.PNG_Reader_3.SetDataExtent(0, 180, 0, 180, 0, 179)
        self.PNG_Reader_3.SetFilePrefix(self.filefolder_3+'/')
        self.PNG_Reader_3.SetFilePattern("%s%d.png")
        self.PNG_Reader_3.Update()
        self.PNG_Reader_3.SetDataByteOrderToLittleEndian()

        self.PNG_contour_3 = vtk.vtkDiscreteMarchingCubes()
        self.PNG_contour_3.SetInputConnection(self.PNG_Reader_3.GetOutputPort())
        self.PNG_contour_3.ComputeNormalsOn()
        self.PNG_contour_3.SetValue(0, 255)

        self.PNG_sinc_3 = vtk.vtkWindowedSincPolyDataFilter()
        self.PNG_sinc_3.SetInputConnection(self.PNG_contour_3.GetOutputPort())
        self.PNG_sinc_3.SetNumberOfIterations(50)
        self.PNG_sinc_3.SetPassBand(0.003)

        PNG_mapper_3 = vtk.vtkPolyDataMapper()
        PNG_mapper_3.SetInputConnection(self.PNG_sinc_3.GetOutputPort())
        PNG_mapper_3.ScalarVisibilityOff()

        PNG_actor_3 = vtk.vtkActor()
        PNG_actor_3.SetMapper(PNG_mapper_3)

        PNG_renderer_3 = vtk.vtkRenderer()
        PNG_renderer_3.SetBackground([0.1, 0.1, 0.1])
        PNG_renderer_3.AddActor(PNG_actor_3)

        cameraR_3 = vtk.vtkCamera()
        cameraR_3.SetPosition(0, 1000, 0)
        cameraR_3.SetFocalPoint(0, 0, 0)
        cameraR_3.SetViewUp(0, 0, -1.0)

        self.ren_3.SetActiveCamera(cameraR_3)
        self.ren_3.AddActor(PNG_actor_3)
        self.ren_3.ResetCamera()
        self.iren_3.Initialize()
        self.iren_3.Start()

    def update(self):
        self.ren_1.RemoveAllViewProps()
        self.ren_2.RemoveAllViewProps()
        self.ren_3.RemoveAllViewProps()
        self.ren_all.RemoveAllViewProps()

        self.update_PNG_contour_1 = vtk.vtkDiscreteMarchingCubes()
        self.update_PNG_contour_1.SetInputConnection(self.PNG_Reader_1.GetOutputPort())
        self.update_PNG_contour_1.ComputeNormalsOn()
        self.update_PNG_contour_1.SetValue(0, 255)

        self.updatePNG_sinc_1 = vtk.vtkWindowedSincPolyDataFilter()
        self.updatePNG_sinc_1.SetInputConnection(self.update_PNG_contour_1.GetOutputPort())
        self.updatePNG_sinc_1.SetNumberOfIterations(50)
        self.updatePNG_sinc_1.SetPassBand(0.003)

        updatePNG_transform_1 = vtk.vtkTransform()
        updatePNG_transform_1.RotateWXYZ(self.rotX_1.value(), 1, 0, 0)
        updatePNG_transform_1.RotateWXYZ(-(self.rotY_1.value()), 0, 1, 0)
        updatePNG_transform_1.RotateWXYZ(self.rotZ_1.value(), 0, 0, 1)

        updatePNG_transformFilter_1 = vtk.vtkTransformPolyDataFilter()
        updatePNG_transformFilter_1.SetInputConnection(self.updatePNG_sinc_1.GetOutputPort())
        updatePNG_transformFilter_1.SetTransform(updatePNG_transform_1)
        updatePNG_transformFilter_1.Update()

        update_PNG_mapper_1 = vtk.vtkPolyDataMapper()
        update_PNG_mapper_1.SetInputConnection(updatePNG_transformFilter_1.GetOutputPort())
        update_PNG_mapper_1.ScalarVisibilityOff()

        update_PNG_actor_1 = vtk.vtkActor()
        update_PNG_actor_1.SetMapper(update_PNG_mapper_1)

        update_PNG_renderer_1 = vtk.vtkRenderer()
        update_PNG_renderer_1.SetBackground([0.1, 0.1, 0.1])
        update_PNG_renderer_1.AddActor(update_PNG_actor_1)

        cameraR = vtk.vtkCamera()
        cameraR.SetPosition(0, 1000, 0)
        cameraR.SetFocalPoint(0, 0, 0)
        cameraR.SetViewUp(0, 0, -1.0)

        self.ren_1.SetActiveCamera(cameraR)
        self.ren_1.AddActor(update_PNG_actor_1)
        self.ren_1.ResetCamera()
        self.iren_1.Initialize()
        self.iren_1.Start()



        self.update_PNG_contour_2 = vtk.vtkDiscreteMarchingCubes()
        self.update_PNG_contour_2.SetInputConnection(self.PNG_Reader_2.GetOutputPort())
        self.update_PNG_contour_2.ComputeNormalsOn()
        self.update_PNG_contour_2.SetValue(0, 255)

        self.updatePNG_sinc_2 = vtk.vtkWindowedSincPolyDataFilter()
        self.updatePNG_sinc_2.SetInputConnection(self.update_PNG_contour_2.GetOutputPort())
        self.updatePNG_sinc_2.SetNumberOfIterations(50)
        self.updatePNG_sinc_2.SetPassBand(0.003)

        updatePNG_transform_2 = vtk.vtkTransform()
        updatePNG_transform_2.RotateWXYZ(self.rotX_2.value(), 1, 0, 0)
        updatePNG_transform_2.RotateWXYZ(-(self.rotY_2.value()), 0, 1, 0)
        updatePNG_transform_2.RotateWXYZ(self.rotZ_2.value(), 0, 0, 1)

        updatePNG_transformFilter_2 = vtk.vtkTransformPolyDataFilter()
        updatePNG_transformFilter_2.SetInputConnection(self.updatePNG_sinc_2.GetOutputPort())
        updatePNG_transformFilter_2.SetTransform(updatePNG_transform_2)
        updatePNG_transformFilter_2.Update()

        update_PNG_mapper_2 = vtk.vtkPolyDataMapper()
        update_PNG_mapper_2.SetInputConnection(updatePNG_transformFilter_2.GetOutputPort())
        update_PNG_mapper_2.ScalarVisibilityOff()

        update_PNG_actor_2 = vtk.vtkActor()
        update_PNG_actor_2.SetMapper(update_PNG_mapper_2)

        update_PNG_renderer_2 = vtk.vtkRenderer()
        update_PNG_renderer_2.SetBackground([0.1, 0.1, 0.1])
        update_PNG_renderer_2.AddActor(update_PNG_actor_2)

        cameraR = vtk.vtkCamera()
        cameraR.SetPosition(0, 1000, 0)
        cameraR.SetFocalPoint(0, 0, 0)
        cameraR.SetViewUp(0, 0, -1.0)

        self.ren_2.SetActiveCamera(cameraR)
        self.ren_2.AddActor(update_PNG_actor_2)
        self.ren_2.ResetCamera()
        self.iren_2.Initialize()
        self.iren_2.Start()

        self.update_PNG_contour_3 = vtk.vtkDiscreteMarchingCubes()
        self.update_PNG_contour_3.SetInputConnection(self.PNG_Reader_3.GetOutputPort())
        self.update_PNG_contour_3.ComputeNormalsOn()
        self.update_PNG_contour_3.SetValue(0, 255)

        self.updatePNG_sinc_3 = vtk.vtkWindowedSincPolyDataFilter()
        self.updatePNG_sinc_3.SetInputConnection(self.update_PNG_contour_3.GetOutputPort())
        self.updatePNG_sinc_3.SetNumberOfIterations(50)
        self.updatePNG_sinc_3.SetPassBand(0.003)

        updatePNG_transform_3 = vtk.vtkTransform()
        updatePNG_transform_3.RotateWXYZ(self.rotX_3.value(), 1, 0, 0)
        updatePNG_transform_3.RotateWXYZ(-(self.rotY_3.value()), 0, 1, 0)
        updatePNG_transform_3.RotateWXYZ(self.rotZ_3.value(), 0, 0, 1)

        updatePNG_transformFilter_3 = vtk.vtkTransformPolyDataFilter()
        updatePNG_transformFilter_3.SetInputConnection(self.updatePNG_sinc_3.GetOutputPort())
        updatePNG_transformFilter_3.SetTransform(updatePNG_transform_3)
        updatePNG_transformFilter_3.Update()

        update_PNG_mapper_3 = vtk.vtkPolyDataMapper()
        update_PNG_mapper_3.SetInputConnection(updatePNG_transformFilter_3.GetOutputPort())
        update_PNG_mapper_3.ScalarVisibilityOff()

        update_PNG_actor_3 = vtk.vtkActor()
        update_PNG_actor_3.SetMapper(update_PNG_mapper_3)

        update_PNG_renderer_3 = vtk.vtkRenderer()
        update_PNG_renderer_3.SetBackground([0.1, 0.1, 0.1])
        update_PNG_renderer_3.AddActor(update_PNG_actor_3)

        cameraR = vtk.vtkCamera()
        cameraR.SetPosition(0, 1000, 0)
        cameraR.SetFocalPoint(0, 0, 0)
        cameraR.SetViewUp(0, 0, -1.0)

        self.ren_3.SetActiveCamera(cameraR)
        self.ren_3.AddActor(update_PNG_actor_3)
        self.ren_3.ResetCamera()
        self.iren_3.Initialize()
        self.iren_3.Start()

        print('--------ok--------1')
        self.volumearray_1 = self.pngtopoint(self.filefolder_1)
        self.volumearray_2 = self.pngtopoint(self.filefolder_2)
        self.volumearray_3 = self.pngtopoint(self.filefolder_3)
        print('--------ok--------11')
        self.PCsourcedata_1 = self.volumearray_1
        self.PCpoints_1 = vtk.vtkPoints()
        self.PCpoints_1.SetData(numpy_to_vtk(self.PCsourcedata_1))
        PCpolydata_1 = vtk.vtkPolyData()
        PCpolydata_1.SetPoints(self.PCpoints_1)
        PCvertex_1 = vtk.vtkPolyDataPointSampler()
        PCvertex_1.SetInputData(PCpolydata_1)
        PCtransform_1 = vtk.vtkTransform()
        print('--------ok--------12')
        PCtransform_1.RotateWXYZ(self.rotZ_1.value(), 1, 0, 0)
        PCtransform_1.RotateWXYZ(self.rotY_1.value(), 0, 1, 0)
        PCtransform_1.RotateWXYZ(self.rotX_1.value(), 0, 0, 1)
        print('--------ok--------13')
        PCtransformFilter_1 = vtk.vtkTransformPolyDataFilter()
        PCtransformFilter_1.SetInputConnection(PCvertex_1.GetOutputPort())
        PCtransformFilter_1.SetTransform(PCtransform_1)
        PCtransformFilter_1.Update()
        print('--------ok--------14')
        vtkarray_1 = PCtransformFilter_1.GetOutput().GetPoints().GetData()
        nparray_1 = vtk_to_numpy(vtkarray_1)
        maskvol_1 = nparray_1.astype(int)
        print('--------ok--------15')
        maskvol_1[..., 0] += 180
        maskvol_1[..., 1] += 180
        maskvol_1[..., 2] += 180
        masktemp_1 = np.zeros((360, 360, 360))
        print('--------ok--------16')
        a = masktemp_1 > 0
        b = masktemp_1 < 360
        c = a * b
        d = c[:, 0] * c[:, 1] * c[:, 2]
        dex = np.argwhere(d == False)
        maskvol_1 = np.delete(maskvol_1, dex, axis=0)
        print('--------ok--------17')
        maskvol_1[maskvol_1[:, 0], maskvol_1[:, 1], maskvol_1[:, 2]] = 255

        print('--------ok--------2')
        self.PCsourcedata_2 = self.volumearray_2
        self.PCpoints_2 = vtk.vtkPoints()
        self.PCpoints_2.SetData(numpy_to_vtk(self.PCsourcedata_2))
        PCpolydata_2 = vtk.vtkPolyData()
        PCpolydata_2.SetPoints(self.PCpoints_2)
        PCvertex_2 = vtk.vtkPolyDataPointSampler()
        PCvertex_2.SetInputData(PCpolydata_2)
        PCtransform_2 = vtk.vtkTransform()

        PCtransform_2.RotateWXYZ(self.rotZ_2.value(), 1, 0, 0)
        PCtransform_2.RotateWXYZ(self.rotY_2.value(), 0, 1, 0)
        PCtransform_2.RotateWXYZ(self.rotX_2.value(), 0, 0, 1)

        print('--------ok--------3')
        PCtransformFilter_2 = vtk.vtkTransformPolyDataFilter()
        PCtransformFilter_2.SetInputConnection(PCvertex_2.GetOutputPort())
        PCtransformFilter_2.SetTransform(PCtransform_2)
        PCtransformFilter_2.Update()

        vtkarray_2 = PCtransformFilter_2.GetOutput().GetPoints().GetData()
        nparray_2 = vtk_to_numpy(vtkarray_2)
        maskvol_2 = nparray_2.astype(int)
        maskvol_2[..., 0] += 180
        maskvol_2[..., 1] += 180
        maskvol_2[..., 2] += 180
        masktemp_2 = np.zeros((360, 360, 360))
        a = masktemp_2 > 0
        b = masktemp_2 < 360
        c = a * b
        d = c[:, 0] * c[:, 1] * c[:, 2]
        dex = np.argwhere(d == False)
        maskvol_2 = np.delete(maskvol_2, dex, axis=0)
        maskvol_2[maskvol_2[:, 0], maskvol_2[:, 1], maskvol_2[:, 2]] = 255


        self.PCsourcedata_3 = self.volumearray_3
        self.PCpoints_3 = vtk.vtkPoints()
        self.PCpoints_3.SetData(numpy_to_vtk(self.PCsourcedata_3))
        PCpolydata_3 = vtk.vtkPolyData()
        PCpolydata_3.SetPoints(self.PCpoints_3)
        PCvertex_3 = vtk.vtkPolyDataPointSampler()
        PCvertex_3.SetInputData(PCpolydata_3)
        PCtransform_3 = vtk.vtkTransform()

        PCtransform_3.RotateWXYZ(self.rotZ_3.value(), 1, 0, 0)
        PCtransform_3.RotateWXYZ(self.rotY_3.value(), 0, 1, 0)
        PCtransform_3.RotateWXYZ(self.rotX_3.value(), 0, 0, 1)

        print('--------ok--------4')
        PCtransformFilter_3 = vtk.vtkTransformPolyDataFilter()
        PCtransformFilter_3.SetInputConnection(PCvertex_3.GetOutputPort())
        PCtransformFilter_3.SetTransform(PCtransform_3)
        PCtransformFilter_3.Update()

        vtkarray_3 = PCtransformFilter_3.GetOutput().GetPoints().GetData()
        nparray_3 = vtk_to_numpy(vtkarray_3)
        maskvol_3 = nparray_3.astype(int)
        maskvol_3[..., 0] += 180
        maskvol_3[..., 1] += 180
        maskvol_3[..., 2] += 180
        masktemp_3 = np.zeros((360, 360, 360))
        a = masktemp_3 > 0
        b = masktemp_3 < 360
        c = a * b
        d = c[:, 0] * c[:, 1] * c[:, 2]
        dex = np.argwhere(d == False)
        maskvol_3 = np.delete(maskvol_3, dex, axis=0)
        maskvol_3[maskvol_3[:, 0], maskvol_3[:, 1], maskvol_3[:, 2]] = 255

        print('--------ok--------5')

        for x, i in enumerate(range(0, maskvol_1.shape[0], 2)):
            img = maskvol_1[i]
            img = img.astype(np.uint8)
            img = cv2.resize(img, (180,180))
            img = np.where(img>1,255, 0)
            self.bone_1[x] = img
        for x, i in enumerate(range(0, maskvol_2.shape[0], 2)):
            img = maskvol_2[i]
            img = img.astype(np.uint8)
            img = cv2.resize(img, (180,180))
            img = np.where(img>1,255, 0)
            self.bone_2[x] = img
        for x, i in enumerate(range(0, maskvol_3.shape[0], 2)):
            img = maskvol_3[i]
            img = img.astype(np.uint8)
            img = cv2.resize(img, (180,180))
            img = np.where(img>1,255, 0)
            self.bone_3[x] = img


        self.allvolume = np.zeros((180, 180, 180))
        self.allvolume[21:81] += self.bone_1[65:116]
        self.allvolume[60:120] += self.bone_2[65:116]
        self.allvolume[99:159] += self.bone_3[65:116]
        self.allvolume = np.where(self.allvolume>128, 255, 0)
        self.allvolume = self.allvolume.astype(np.uint8)

        for i in range(self.allvolume.shape[0]):
            temp = self.allvolume[i]
            cv2.imwrite(os.path.join('./temp_simulation', str(i)+'.png'), temp)

        self.PNG_Reader_all = vtk.vtkPNGReader()
        self.PNG_Reader_all.SetNumberOfScalarComponents(1)
        self.PNG_Reader_all.SetFileDimensionality(3)
        self.PNG_Reader_all.SetDataExtent(0, 180, 0, 180, 0, 179)
        self.PNG_Reader_all.SetFilePrefix('./temp_simulation/')
        self.PNG_Reader_all.SetFilePattern("%s%d.png")
        self.PNG_Reader_all.Update()
        self.PNG_Reader_all.SetDataByteOrderToLittleEndian()

        self.PNG_contour_all = vtk.vtkDiscreteMarchingCubes()
        self.PNG_contour_all.SetInputConnection(self.PNG_Reader_all.GetOutputPort())
        self.PNG_contour_all.ComputeNormalsOn()
        self.PNG_contour_all.SetValue(0, 255)

        self.PNG_sinc_all = vtk.vtkWindowedSincPolyDataFilter()
        self.PNG_sinc_all.SetInputConnection(self.PNG_contour_all.GetOutputPort())
        self.PNG_sinc_all.SetNumberOfIterations(50)
        self.PNG_sinc_all.SetPassBand(0.003)

        PNG_mapper_all = vtk.vtkPolyDataMapper()
        PNG_mapper_all.SetInputConnection(self.PNG_sinc_all.GetOutputPort())
        PNG_mapper_all.ScalarVisibilityOff()

        PNG_actor_all = vtk.vtkActor()
        PNG_actor_all.SetMapper(PNG_mapper_all)

        PNG_renderer_all = vtk.vtkRenderer()
        PNG_renderer_all.SetBackground([0.1, 0.1, 0.1])
        PNG_renderer_all.AddActor(PNG_actor_all)

        cameraR_all = vtk.vtkCamera()
        cameraR_all.SetPosition(0, 1000, 0)
        cameraR_all.SetFocalPoint(0, 0, 0)
        cameraR_all.SetViewUp(0, 0, -1.0)

        self.ren_all.SetActiveCamera(cameraR_all)
        self.ren_all.AddActor(PNG_actor_all)
        self.ren_all.ResetCamera()
        self.iren_all.Initialize()
        self.iren_all.Start()


        self.PC_source_data = temp
        # 新建 vtkPoints 实例
        self.PC_points = vtk.vtkPoints()
        # 导入点数据
        self.PC_points.SetData(numpy_to_vtk(self.PC_source_data))







    def pngtopoint(self, filepath):
        file_folder = os.listdir(filepath)
        file_folder.sort(key=lambda x: int(x.split('.png')[0]))
        maskvolume_array = np.zeros((180, 180, 180))
        for i, x in enumerate(file_folder):
            img = cv2.imread(os.path.join(filepath, x), 0)
            maskvolume_array[i] = img

        img_tensor = torch.from_numpy(maskvolume_array)
        img_tensor = img_tensor.unsqueeze(0)
        img_tensor = img_tensor.unsqueeze(0)
        img_interporlate_tensor = F.interpolate(img_tensor, scale_factor=2, mode='nearest')
        img_interporlate_tensor = img_interporlate_tensor.squeeze(0)
        img_interporlate_tensor = img_interporlate_tensor.squeeze(0)
        img_interporlate_array = img_interporlate_tensor.numpy()
        index = np.argwhere(img_interporlate_array == 255)

        temp = np.zeros(index.shape)
        temp[..., 0] = index[..., 0]-180
        temp[..., 1] = index[..., 1]-180
        temp[..., 2] = index[..., 2]-180
        return temp







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveBTN.setText(_translate("MainWindow", "Save"))
        self.label_3.setText(_translate("MainWindow", "Rotation X :"))
        self.label_4.setText(_translate("MainWindow", "Rotation Y :"))
        self.label_5.setText(_translate("MainWindow", "Rotation Z :"))
        self.updateBTN.setText(_translate("MainWindow", "Update"))
        self.label_6.setText(_translate("MainWindow", "Spine"))
        self.label_8.setText(_translate("MainWindow", "Fluoroscopy"))
        self.label_2.setText(_translate("MainWindow", "Translate Y :"))
        self.label.setText(_translate("MainWindow", "Translate X :"))
        self.TransZ_label.setText(_translate("MainWindow", "0"))
        self.TransY_label.setText(_translate("MainWindow", "0"))
        self.TransX_label.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Translate Z :"))
        self.RotX_label.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "Roration Z :"))
        self.label_7.setText(_translate("MainWindow", "Roration X :"))
        self.RotY_label.setText(_translate("MainWindow", "0"))
        self.RotsZ_label.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Roration Y :"))
        self.label_10.setText(_translate("MainWindow", "Fluoroscopy"))
        self.UpdateAllBTN.setText(_translate("MainWindow", "Fresh"))
        self.Load1BTN.setText(_translate("MainWindow", "load"))
        self.Load2BTN.setText(_translate("MainWindow", "load"))
        self.Load3BTN.setText(_translate("MainWindow", "load"))



if __name__ == '__main__':
    import sys
    import os
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())



