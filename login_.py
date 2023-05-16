
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setWindowIcon(QtGui.QIcon('calculator-icon_34473.ico'))
        login_form.setObjectName("login_form")
        login_form.resize(275, 135)
        login_form.setStyleSheet("QWidget {\n"
"  background-color: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"\n"
"QLabel#heading {\n"
"  color: #0f1925;\n"
"  font-size: 18px;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QLabel#subheading {\n"
"  color: #0f1925;\n"
"  font-size: 12px;\n"
"  font-weight: normal;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #0d6efd;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=login_form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.login_bt = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_bt.sizePolicy().hasHeightForWidth())
        self.login_bt.setSizePolicy(sizePolicy)
        self.login_bt.setStyleSheet("")
        self.login_bt.setObjectName("login_bt")
        self.gridLayout.addWidget(self.login_bt, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.cancel_bt = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_bt.sizePolicy().hasHeightForWidth())
        self.cancel_bt.setSizePolicy(sizePolicy)
        self.cancel_bt.setObjectName("cancel_bt")
        self.gridLayout.addWidget(self.cancel_bt, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.id_label = QtWidgets.QLabel(parent=self.widget)
        self.id_label.setObjectName("id_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.id_label)
        self.id_lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.id_lineEdit.setObjectName("id_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.id_lineEdit)
        self.password_label = QtWidgets.QLabel(parent=self.widget)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.password_label)
        self.password_lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.password_lineEdit.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.password_lineEdit)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 5)
        login_form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=login_form)
        self.statusbar.setObjectName("statusbar")
        login_form.setStatusBar(self.statusbar)

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)

        self.cancel_bt.clicked.connect(QtCore.QCoreApplication.instance().quit)
        

    def retranslateUi(self, login_form):
        _translate = QtCore.QCoreApplication.translate
        login_form.setWindowTitle(_translate("login_form", "Login form"))
        self.login_bt.setText(_translate("login_form", "Login"))
        self.cancel_bt.setText(_translate("login_form", "Cancel"))
        self.id_label.setText(_translate("login_form", "ID:"))
        self.password_label.setText(_translate("login_form", "Password:"))
