import os, sys
from PyQt5.QtWidgets import *

from templete.tabela import Ui_Tabela
from modulos.Cadastrar import Cadastrar
from db.Query import Sqlite_Db;


class Tabela(QMainWindow):
    def __init__(self,*argv,**argvs):
        super(Tabela,self).__init__(*argv,**argvs)
        self.ui = Ui_Tabela()
        self.ui.setupUi(self)
        self.ui.actionCadastra.triggered.connect(self.add)
        self.carregarDados()
    
    def carregarDados(self):
        db = Sqlite_Db("EMPRESA.db")
        listaFuncionario = db.sqlQuery2("select * from funcionario")
        #for func in listaFuncionario:
         #   print(func)
        self.ui.tableWidget.setRowCount(0)
        #print(list(enumerate(listaFuncionario)))
        for linha, dados in enumerate(listaFuncionario): #enumerate enumera a lista ["a","b","c"] = [(0,"a"),(1,"b"),(2,"c")]
            self.ui.tableWidget.insertRow(linha)
            #print(list(enumerate(dados)))
            for coluna, valores in enumerate(dados):
                self.ui.tableWidget.setItem(linha,coluna,QTableWidgetItem(str(valores)))
    
    def add(self):
        #c = Cadastrar()
        #c.exec_()
        self.window = Cadastrar()
        self.window.show()