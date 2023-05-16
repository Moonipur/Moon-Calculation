
from PyQt6 import QtCore, QtGui, QtWidgets
from op_cl import count_sym, check_dot, calc_percent


class Ui_moon_calc(object):
    def setupUi(self, moon_calc):
        moon_calc.setWindowIcon(QtGui.QIcon('calculator-icon_34473.ico'))
        moon_calc.setObjectName("moon_calc")
        moon_calc.resize(356, 240)
        moon_calc.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(moon_calc)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_calc = QtWidgets.QLabel(parent=moon_calc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_calc.setFont(font)
        self.list_calc.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.list_calc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.list_calc.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.list_calc.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.list_calc.setObjectName("list_calc")
        self.verticalLayout.addWidget(self.list_calc)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.bt_1 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("1"))
        self.bt_1.setObjectName("bt_1")
        self.gridLayout.addWidget(self.bt_1, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.bt_9 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("9"))
        self.bt_9.setObjectName("bt_9")
        self.gridLayout.addWidget(self.bt_9, 2, 4, 1, 1)
        self.bt_3 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("3"))
        self.bt_3.setObjectName("bt_3")
        self.gridLayout.addWidget(self.bt_3, 6, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.bt_7 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("7"))
        self.bt_7.setObjectName("bt_7")
        self.gridLayout.addWidget(self.bt_7, 2, 0, 1, 1)
        self.bt_0 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("0"))
        self.bt_0.setObjectName("bt_0")
        self.gridLayout.addWidget(self.bt_0, 8, 0, 1, 1)
        self.bt_5 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("5"))
        self.bt_5.setObjectName("bt_5")
        self.gridLayout.addWidget(self.bt_5, 4, 2, 1, 1)
        self.percent_bt = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.accessory_sym("%"))
        self.percent_bt.setObjectName("percent_bt")
        self.gridLayout.addWidget(self.percent_bt, 0, 4, 1, 1)
        self.open_bt = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.accessory_sym("("))
        self.open_bt.setEnabled(True)
        self.open_bt.setObjectName("open_bt")
        self.gridLayout.addWidget(self.open_bt, 0, 0, 1, 1)
        self.close_bt = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.accessory_sym(")"))
        self.close_bt.setObjectName("close_bt")
        self.gridLayout.addWidget(self.close_bt, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.plus_bt = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_operator("+"))
        self.plus_bt.setObjectName("plus_bt")
        self.gridLayout.addWidget(self.plus_bt, 8, 6, 1, 1)
        self.minus_bt = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_operator("-"))
        self.minus_bt.setObjectName("minus_bt")
        self.gridLayout.addWidget(self.minus_bt, 6, 6, 1, 1)
        self.bt_4 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("4"))
        self.bt_4.setObjectName("bt_4")
        self.gridLayout.addWidget(self.bt_4, 4, 0, 1, 1)
        self.multiply_bt = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_operator("*"))
        self.multiply_bt.setObjectName("multiply_bt")
        self.gridLayout.addWidget(self.multiply_bt, 4, 6, 1, 1)
        self.equal_bt = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_calc())
        self.equal_bt.setObjectName("equal_bt")
        self.gridLayout.addWidget(self.equal_bt, 8, 4, 1, 1)
        self.bt_2 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("2"))
        self.bt_2.setObjectName("bt_2")
        self.gridLayout.addWidget(self.bt_2, 6, 2, 1, 1)
        self.bt_6 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("6"))
        self.bt_6.setObjectName("bt_6")
        self.gridLayout.addWidget(self.bt_6, 4, 4, 1, 1)
        self.bt_point = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_dot())
        self.bt_point.setObjectName("bt_point")
        self.gridLayout.addWidget(self.bt_point, 8, 2, 1, 1)
        self.clear_bt = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("AC"))
        self.clear_bt.setObjectName("clear_bt")
        self.gridLayout.addWidget(self.clear_bt, 0, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 3, 1, 1)
        self.devide_bt = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_operator("/"))
        self.devide_bt.setObjectName("devide_bt")
        self.gridLayout.addWidget(self.devide_bt, 2, 6, 1, 1)
        self.bt_8 = QtWidgets.QPushButton(parent=moon_calc, clicked= lambda: self.press_bt("8"))
        self.bt_8.setObjectName("bt_8")
        self.gridLayout.addWidget(self.bt_8, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem6, 7, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem7, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(moon_calc)
        QtCore.QMetaObject.connectSlotsByName(moon_calc)

    def press_operator(self, op):
        last_screen = self.list_calc.text()
        if op in ['+', '-']:
            if self.list_calc.text() == "0":
                self.list_calc.setText("")
                self.list_calc.setText(f'{self.list_calc.text()}{op}')
            else:
                if last_screen[-1] in ['+', '-']:
                    pass
                else:
                    self.list_calc.setText(f'{last_screen}{op}')
        elif op in ['*', '/']:
            if last_screen[-1] in ['+', '-', '*', '/']:
                pass
            else:
                self.list_calc.setText(f'{last_screen}{op}')
    
    def accessory_sym(self, sym):
        last_screen = self.list_calc.text()
        if sym == '(':
            if last_screen == '0':
                self.list_calc.setText('')
                self.list_calc.setText(f'{self.list_calc.text()}{sym}')
            elif last_screen[-1] in ['(']:
                pass
            else:
                self.list_calc.setText(f'{last_screen}{sym}')
        elif sym == ')':
            if last_screen[-1] in ['(', '+', '-', '*', '/']:
                pass
            else:
                if count_sym(last_screen) == True:
                    self.list_calc.setText(f'{last_screen}{sym}')
                else:
                    pass
        elif sym == '%':
            if last_screen[-1] in ['(', '+', '-', '*', '/', '.', ')']:
                pass
            elif last_screen == '0':
                pass
            else:
                self.list_calc.setText(f'{last_screen}{sym}')

    def press_dot(self):
        last_screen = self.list_calc.text()
        if '.' in last_screen:
            if check_dot(last_screen) == True:
                self.list_calc.setText(f'{last_screen}.')
            elif last_screen[-1] in ['+','-','*','/','(',')']:
                self.list_calc.setText(f'{last_screen}.')
            else:
                pass
        else:
            self.list_calc.setText(f'{last_screen}.')

    def press_bt(self, pressed):
        last_screen = self.list_calc.text()
        if pressed != 'AC':
            if last_screen in ["0", "-0", "+0"]:
                if last_screen == "-0":
                    self.list_calc.setText("-")
                elif last_screen == "+0":
                    self.list_calc.setText("+")
                elif last_screen == "0":
                    self.list_calc.setText("")
                self.list_calc.setText(f'{self.list_calc.text()}{pressed}')
            else:
                self.list_calc.setText(f'{self.list_calc.text()}{pressed}')
        else:
            self.list_calc.setText("0")

    def press_calc(self):
        last_screen = self.list_calc.text()
        if '%' not in last_screen:
            try:
                answer = eval(last_screen)
                self.list_calc.setText(f'{answer}')
            except:
                self.list_calc.setText('ERROR')
        else:
            try:
                answer = calc_percent(last_screen)
                self.list_calc.setText(f'{answer}')
            except:
                self.list_calc.setText('ERROR')


    def retranslateUi(self, moon_calc):
        _translate = QtCore.QCoreApplication.translate
        moon_calc.setWindowTitle(_translate("moon_calc", "Moon calculator"))
        self.list_calc.setText(_translate("moon_calc", "0"))
        self.bt_1.setText(_translate("moon_calc", "1"))
        self.bt_9.setText(_translate("moon_calc", "9"))
        self.bt_3.setText(_translate("moon_calc", "3"))
        self.bt_7.setText(_translate("moon_calc", "7"))
        self.bt_0.setText(_translate("moon_calc", "0"))
        self.bt_5.setText(_translate("moon_calc", "5"))
        self.percent_bt.setText(_translate("moon_calc", "%"))
        self.open_bt.setText(_translate("moon_calc", "("))
        self.close_bt.setText(_translate("moon_calc", ")"))
        self.plus_bt.setText(_translate("moon_calc", "+"))
        self.minus_bt.setText(_translate("moon_calc", "-"))
        self.bt_4.setText(_translate("moon_calc", "4"))
        self.multiply_bt.setText(_translate("moon_calc", "*"))
        self.equal_bt.setText(_translate("moon_calc", "="))
        self.bt_2.setText(_translate("moon_calc", "2"))
        self.bt_6.setText(_translate("moon_calc", "6"))
        self.bt_point.setText(_translate("moon_calc", "."))
        self.clear_bt.setText(_translate("moon_calc", "AC"))
        self.devide_bt.setText(_translate("moon_calc", "/"))
        self.bt_8.setText(_translate("moon_calc", "8"))
