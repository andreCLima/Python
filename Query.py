import sqlite3

class Sqlite_Db:
    def __init__(self,banco = None): #valor defalt
        self.conn = None
        self.cursor = None
        if banco:
            self.open(banco)
    
    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco) # conecta ou cria o banco
            self.cursor = self.conn.cursor()
            print( "Banco Criado")
        except sqlite3.Error as e:
            print( "Erro ao criar o banco %s" %(e))

    def criarTabela(self,nome): #"""" permite saltar linhas
        self.cursor.execute("""
            CREATE TABLE %s(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME TEXT NOT NULL,
                FUNCAO TEXT NOT NULL,
                USER TEXT NOT NULL,
                PASSWD TEXT NOT NULL
            ) 
        """%(nome))
    
    def sqlQuery1(self, query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()
        print("Dados inseridos com sucesso")
    
    def sqlQuery2(self, query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall() #para select que tem retorno


#dados = Sqlite_Db("EMPRESA.db")
#db.criarTabela("FUNCIONARIO")

#db.sqlQuery1("INSERT INTO FUNCIONARIO(NOME, FUNCAO, USER, PASSWD) VALUES ('ANDRE','PROGRAMADOR','AND','4321')")
#dados.sqlQuery2("SELECT * FROM FUNCIONARIO WHERE USER = '{}' AND PASSWD = '{}'".format("AND","1234"))
#print(db.sqlQuery2("SELECT * FROM FUNCIONARIO"))
