import os, sys
from PyQt5.QtWidgets import *

from modulos.Login import Login # para a pasta/arquivo importe class login

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
	window = Login()
	window.show()
sys.exit(app.exec_())