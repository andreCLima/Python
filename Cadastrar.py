from typing import Text
from db.Query import Sqlite_Db
import os, sys
from PyQt5.QtWidgets import *

from templete.cadastrar import Ui_Cadastrar

class Cadastrar(QDialog):
    def __init__(self,*argv,**argvs):
        super(Cadastrar,self).__init__(*argv,**argvs)
        self.ui = Ui_Cadastrar()
        self.ui.setupUi(self)
        self.ui.butCadastrar.clicked.connect(self.add)
        self.ui.butCancelar.clicked.connect(self.cam)
        self.ui.butLimpar.clicked.connect(self.limpar)
    
    
    def add(self):
        con = Sqlite_Db("Empresa.db")
        nome = self.ui.edtNome.text()
        funcao = self.ui.edtFuncao.text()
        user = "admin"
        passwd = "admin"
        con.sqlQuery1("""
            INSERT INTO FUNCIONARIO(NOME, FUNCAO, USER, PASSWD)
            VALUES('{}','{}','{}','{}')
        """.format(nome,funcao,user,passwd))
        QMessageBox.information(QMessageBox(),"Info","Gravado com sucesso")
        
    def cam(self):
        self.limpar()
        self.close()

    def limpar(self):
        self.ui.edtCodigo.clear()
        self.ui.edtFuncao.clear()
        self.ui.edtNome.clear()

