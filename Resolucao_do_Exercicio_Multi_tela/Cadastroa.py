# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Cadastro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 250)
        MainWindow.setMinimumSize(QtCore.QSize(300, 250))
        MainWindow.setStyleSheet("background-color: rgb(99, 99, 99);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_cadastro = QtWidgets.QLabel(self.frame)
        self.label_cadastro.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadastro.setFont(font)
        self.label_cadastro.setStyleSheet("color: rgb(230, 230, 230);\n"
"margin-left: 100px;\n"
"margin-right: 100px;\n"
"")
        self.label_cadastro.setObjectName("label_cadastro")
        self.horizontalLayout.addWidget(self.label_cadastro)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_cadastro_nome = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadastro_nome.setFont(font)
        self.label_cadastro_nome.setStyleSheet("color: rgb(230, 230, 230);")
        self.label_cadastro_nome.setObjectName("label_cadastro_nome")
        self.verticalLayout_3.addWidget(self.label_cadastro_nome)
        self.label_cadastro_endereco = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadastro_endereco.setFont(font)
        self.label_cadastro_endereco.setStyleSheet("color: rgb(230, 230, 230);")
        self.label_cadastro_endereco.setObjectName("label_cadastro_endereco")
        self.verticalLayout_3.addWidget(self.label_cadastro_endereco)
        self.label_cadastro_cpf = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadastro_cpf.setFont(font)
        self.label_cadastro_cpf.setStyleSheet("color: rgb(230, 230, 230);")
        self.label_cadastro_cpf.setObjectName("label_cadastro_cpf")
        self.verticalLayout_3.addWidget(self.label_cadastro_cpf)
        self.label_cadastro_nascimento = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadastro_nascimento.setFont(font)
        self.label_cadastro_nascimento.setStyleSheet("color: rgb(230, 230, 230);")
        self.label_cadastro_nascimento.setObjectName("label_cadastro_nascimento")
        self.verticalLayout_3.addWidget(self.label_cadastro_nascimento)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_cadastro_nome = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_cadastro_nome.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding 15px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(230, 230, 230);\n"
"}")
        self.lineEdit_cadastro_nome.setObjectName("lineEdit_cadastro_nome")
        self.verticalLayout_2.addWidget(self.lineEdit_cadastro_nome)
        self.lineEdit_cadastro_endereco = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_cadastro_endereco.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding 15px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(230, 230, 230);\n"
"}")
        self.lineEdit_cadastro_endereco.setObjectName("lineEdit_cadastro_endereco")
        self.verticalLayout_2.addWidget(self.lineEdit_cadastro_endereco)
        self.lineEdit_cadastro_cpf = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_cadastro_cpf.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding 15px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(230, 230, 230);\n"
"}")
        self.lineEdit_cadastro_cpf.setObjectName("lineEdit_cadastro_cpf")
        self.verticalLayout_2.addWidget(self.lineEdit_cadastro_cpf)
        self.lineEdit_cadastro_nascimento = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_cadastro_nascimento.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding 15px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(230, 230, 230);\n"
"}")
        self.lineEdit_cadastro_nascimento.setObjectName("lineEdit_cadastro_nascimento")
        self.verticalLayout_2.addWidget(self.lineEdit_cadastro_nascimento)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_cadastro_cadastrar = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_cadastro_cadastrar.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_cadastro_cadastrar.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-position: center;\n"
"    background-color: rgb(255, 85, 127);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_cadastro_cadastrar.setObjectName("pushButton_cadastro_cadastrar")
        self.verticalLayout_4.addWidget(self.pushButton_cadastro_cadastrar)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_cadastro.setText(_translate("MainWindow", "Cadastro"))
        self.label_cadastro_nome.setText(_translate("MainWindow", "Nome"))
        self.label_cadastro_endereco.setText(_translate("MainWindow", "Endereco"))
        self.label_cadastro_cpf.setText(_translate("MainWindow", "CPF"))
        self.label_cadastro_nascimento.setText(_translate("MainWindow", "Nascimento"))
        self.pushButton_cadastro_cadastrar.setText(_translate("MainWindow", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Cadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
