import sys
import typing
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from login_ import  Ui_login_form
from calc_ import Ui_moon_calc



class MOON_CALC(QWidget):
    def __init__(self):
        super().__init__()
        self.moon_calc = Ui_moon_calc().setupUi(self)
        


class Login_form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = Ui_login_form()
        self.calc = MOON_CALC()

        self.login.setupUi(self)

        self.login.login_bt.clicked.connect(self.authenticate)

    def authenticate(self):
        email = self.login.id_lineEdit.text()
        password = self.login.password_lineEdit.text()

        if email != '' and password == 'CRU0002':
            QMessageBox.information(self, 'Success',"You're logged in!")
            self.win2()
            
        else:
            QMessageBox.critical(self, 'Error',"Invalid email or password.")

    def win2(self):
        self.hide()
        if self.calc.isVisible():
            self.calc.hide()
        else:
            self.calc.show()

app = QApplication(sys.argv)
Win = Login_form()
Win.show()
sys.exit(app.exec())

