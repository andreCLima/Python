#import PyQt5
#from PyQt5 import *

#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

import os, sys

from templete.login import Ui_Login
from modulos.Tabela import Tabela
from db.Query import Sqlite_Db

def msg(txt):
    QMessageBox.information(QMessageBox(),"Informacao",txt)

class Login(QDialog):
    def __init__(self,*argv,**argvs):
        super(Login,self).__init__(*argv,**argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.sair)
    
    def sair(self):
        self.window.close
    
    def login(self):
        con = Sqlite_Db("EMPRESA.db")

        users = self.ui.lineEdit.text()
        passwd = self.ui.lineEdit_2.text()
        #print(users, passwd)
        dados = con.sqlQuery2("""
        SELECT * FROM FUNCIONARIO 
        WHERE USER = '{}' AND PASSWD = '{}'
        """.format(users, passwd))
        if dados:
            print(dados)
            msg("PASSOU DIRETO")
            self.window = Tabela()
            self.window.show()
        else:
            msg("Algo Errado")