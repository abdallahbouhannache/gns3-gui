# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/docker/ui/docker_vm_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DockerVMWizard(object):
    def setupUi(self, DockerVMWizard):
        DockerVMWizard.setObjectName("DockerVMWizard")
        DockerVMWizard.resize(660, 452)
        DockerVMWizard.setModal(True)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiServerWizardPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.uiServerTypeGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.verticalLayout_5.addWidget(self.uiRemoteRadioButton)
        self.uiVMRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiVMRadioButton.setObjectName("uiVMRadioButton")
        self.verticalLayout_5.addWidget(self.uiVMRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.verticalLayout_5.addWidget(self.uiLocalRadioButton)
        self.verticalLayout.addWidget(self.uiServerTypeGroupBox)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_7.addWidget(self.uiRemoteServersLabel, 0, 0, 1, 1)
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_7.addWidget(self.uiRemoteServersComboBox, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.uiRemoteServersGroupBox)
        DockerVMWizard.addPage(self.uiServerWizardPage)
        self.uiImageWizardPage = QtWidgets.QWizardPage()
        self.uiImageWizardPage.setObjectName("uiImageWizardPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiImageWizardPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiExistingImageRadioButton = QtWidgets.QRadioButton(self.uiImageWizardPage)
        self.uiExistingImageRadioButton.setObjectName("uiExistingImageRadioButton")
        self.horizontalLayout_3.addWidget(self.uiExistingImageRadioButton)
        self.uiNewImageRadioButton = QtWidgets.QRadioButton(self.uiImageWizardPage)
        self.uiNewImageRadioButton.setObjectName("uiNewImageRadioButton")
        self.horizontalLayout_3.addWidget(self.uiNewImageRadioButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.uiImageListLabel = QtWidgets.QLabel(self.uiImageWizardPage)
        self.uiImageListLabel.setObjectName("uiImageListLabel")
        self.gridLayout.addWidget(self.uiImageListLabel, 0, 0, 1, 1)
        self.uiImageListComboBox = QtWidgets.QComboBox(self.uiImageWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiImageListComboBox.sizePolicy().hasHeightForWidth())
        self.uiImageListComboBox.setSizePolicy(sizePolicy)
        self.uiImageListComboBox.setObjectName("uiImageListComboBox")
        self.gridLayout.addWidget(self.uiImageListComboBox, 0, 1, 1, 1)
        self.uiImageLineEdit = QtWidgets.QLineEdit(self.uiImageWizardPage)
        self.uiImageLineEdit.setObjectName("uiImageLineEdit")
        self.gridLayout.addWidget(self.uiImageLineEdit, 1, 1, 1, 1)
        self.uiImageNameLabel = QtWidgets.QLabel(self.uiImageWizardPage)
        self.uiImageNameLabel.setObjectName("uiImageNameLabel")
        self.gridLayout.addWidget(self.uiImageNameLabel, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        DockerVMWizard.addPage(self.uiImageWizardPage)
        self.uiNameWizardPage = QtWidgets.QWizardPage()
        self.uiNameWizardPage.setObjectName("uiNameWizardPage")
        self.formLayout = QtWidgets.QFormLayout(self.uiNameWizardPage)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(-1, -1, 0, -1)
        self.formLayout.setObjectName("formLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.uiNameWizardPage)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiNameLabel)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiNameWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNameLineEdit.sizePolicy().hasHeightForWidth())
        self.uiNameLineEdit.setSizePolicy(sizePolicy)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiNameLineEdit)
        DockerVMWizard.addPage(self.uiNameWizardPage)
        self.uiAdaptersWizardPage = QtWidgets.QWizardPage()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdaptersWizardPage.sizePolicy().hasHeightForWidth())
        self.uiAdaptersWizardPage.setSizePolicy(sizePolicy)
        self.uiAdaptersWizardPage.setObjectName("uiAdaptersWizardPage")
        self.formLayout_2 = QtWidgets.QFormLayout(self.uiAdaptersWizardPage)
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.uiAdaptersWizardPage)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.uiAdaptersSpinBox = QtWidgets.QSpinBox(self.uiAdaptersWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdaptersSpinBox.sizePolicy().hasHeightForWidth())
        self.uiAdaptersSpinBox.setSizePolicy(sizePolicy)
        self.uiAdaptersSpinBox.setMinimum(1)
        self.uiAdaptersSpinBox.setObjectName("uiAdaptersSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiAdaptersSpinBox)
        DockerVMWizard.addPage(self.uiAdaptersWizardPage)
        self.uiStartCommandWizardPage = QtWidgets.QWizardPage()
        self.uiStartCommandWizardPage.setObjectName("uiStartCommandWizardPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiStartCommandWizardPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.uiStartCommandWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.uiStartCommandLineEdit = QtWidgets.QLineEdit(self.uiStartCommandWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiStartCommandLineEdit.sizePolicy().hasHeightForWidth())
        self.uiStartCommandLineEdit.setSizePolicy(sizePolicy)
        self.uiStartCommandLineEdit.setObjectName("uiStartCommandLineEdit")
        self.horizontalLayout_2.addWidget(self.uiStartCommandLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        DockerVMWizard.addPage(self.uiStartCommandWizardPage)
        self.uiConsoleWizardPage = QtWidgets.QWizardPage()
        self.uiConsoleWizardPage.setObjectName("uiConsoleWizardPage")
        self.formLayout_3 = QtWidgets.QFormLayout(self.uiConsoleWizardPage)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.uiConsoleWizardPage)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.uiConsoleTypeComboBox = QtWidgets.QComboBox(self.uiConsoleWizardPage)
        self.uiConsoleTypeComboBox.setObjectName("uiConsoleTypeComboBox")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiConsoleTypeComboBox)
        DockerVMWizard.addPage(self.uiConsoleWizardPage)
        self.uiEnvironmentWizardPage = QtWidgets.QWizardPage()
        self.uiEnvironmentWizardPage.setObjectName("uiEnvironmentWizardPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uiEnvironmentWizardPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.uiEnvironmentWizardPage)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.uiEnvironmentWizardPage)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.uiEnvironmentWizardPage)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.uiEnvironmentTextEdit = QtWidgets.QTextEdit(self.uiEnvironmentWizardPage)
        self.uiEnvironmentTextEdit.setObjectName("uiEnvironmentTextEdit")
        self.verticalLayout_4.addWidget(self.uiEnvironmentTextEdit)
        DockerVMWizard.addPage(self.uiEnvironmentWizardPage)

        self.retranslateUi(DockerVMWizard)
        self.uiConsoleTypeComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DockerVMWizard)

    def retranslateUi(self, DockerVMWizard):
        _translate = QtCore.QCoreApplication.translate
        DockerVMWizard.setWindowTitle(_translate("DockerVMWizard", "New Docker VM template"))
        self.uiServerWizardPage.setTitle(_translate("DockerVMWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("DockerVMWizard", "Please choose a server type to run your new Docker VM."))
        self.uiServerTypeGroupBox.setTitle(_translate("DockerVMWizard", "Server type"))
        self.uiRemoteRadioButton.setText(_translate("DockerVMWizard", "Run this Docker VM on a remote computer"))
        self.uiVMRadioButton.setText(_translate("DockerVMWizard", "Run this Docker VM on the GNS3 VM"))
        self.uiLocalRadioButton.setText(_translate("DockerVMWizard", "Run this Docker VM on my local computer"))
        self.uiRemoteServersGroupBox.setTitle(_translate("DockerVMWizard", "Remote server"))
        self.uiRemoteServersLabel.setText(_translate("DockerVMWizard", "Run on:"))
        self.uiImageWizardPage.setTitle(_translate("DockerVMWizard", "Docker Virtual Machine"))
        self.uiImageWizardPage.setSubTitle(_translate("DockerVMWizard", "Please choose a Docker virtual machine from the list or provide an image name on Docker hub."))
        self.uiExistingImageRadioButton.setText(_translate("DockerVMWizard", "Existing image"))
        self.uiNewImageRadioButton.setText(_translate("DockerVMWizard", "New image"))
        self.uiImageListLabel.setText(_translate("DockerVMWizard", "Image list:"))
        self.uiImageNameLabel.setText(_translate("DockerVMWizard", "Image name:"))
        self.uiNameWizardPage.setTitle(_translate("DockerVMWizard", "Container name"))
        self.uiNameWizardPage.setSubTitle(_translate("DockerVMWizard", "Please choose a descriptive name for your new container"))
        self.uiNameLabel.setText(_translate("DockerVMWizard", "Name:"))
        self.uiAdaptersWizardPage.setTitle(_translate("DockerVMWizard", "Network adapters"))
        self.uiAdaptersWizardPage.setSubTitle(_translate("DockerVMWizard", "Number of adapters attached to the container."))
        self.label_2.setText(_translate("DockerVMWizard", "Adapters:"))
        self.uiStartCommandWizardPage.setTitle(_translate("DockerVMWizard", "Start command"))
        self.uiStartCommandWizardPage.setSubTitle(_translate("DockerVMWizard", "Please enter a start command for the container. The default command will be used if you leave this field empty."))
        self.label.setText(_translate("DockerVMWizard", "Start command:"))
        self.uiConsoleWizardPage.setTitle(_translate("DockerVMWizard", "Console type"))
        self.uiConsoleWizardPage.setSubTitle(_translate("DockerVMWizard", "Please choose the console type. Choosing VNC for your container will run a VNC server listening on a port between 5900 and 6000"))
        self.label_6.setText(_translate("DockerVMWizard", "Console type:"))
        self.uiConsoleTypeComboBox.setItemText(0, _translate("DockerVMWizard", "telnet"))
        self.uiConsoleTypeComboBox.setItemText(1, _translate("DockerVMWizard", "vnc"))
        self.uiConsoleTypeComboBox.setItemText(2, _translate("DockerVMWizard", "http"))
        self.uiConsoleTypeComboBox.setItemText(3, _translate("DockerVMWizard", "https"))
        self.uiConsoleTypeComboBox.setItemText(4, _translate("DockerVMWizard", "none"))
        self.uiEnvironmentWizardPage.setTitle(_translate("DockerVMWizard", "Environment"))
        self.uiEnvironmentWizardPage.setSubTitle(_translate("DockerVMWizard", "These variables will be passed to the container. Please read the container documentation to find what variables are used."))
        self.label_3.setText(_translate("DockerVMWizard", "There must be one pair by line, example: "))
        self.label_4.setText(_translate("DockerVMWizard", "MYSQL_HOST=localhost"))
        self.label_5.setText(_translate("DockerVMWizard", "MYSQL_USER=root"))

