from DataBase.MySQL.MySQLDB import mySQL
import mysql.connector
class alunos:
    RA = 0
    nome = ""
    situacao = False
    db = mySQL()
    
    def getAlunos(self):
        sqlGet = f"SELECT RA, nome, situacao FROM alunos WHERE RA = {self.RA}"
        oRS = self.db.execReadQuery(sqlGet)
        for result in oRS:
            self.RA = result[0]
            self.nome = result[1]
            self.situacao = bool(result[2])
    
    def __init__(self, ra, nome = "", situacao = False):
        self.RA = ra
        self.nome = nome
        self.situacao = situacao

    def delete(self):
        sqlDelete = f"DELETE FROM alunos WHERE RA = {self.RA}"
        return self.db.execModQuery(sqlDelete)
    def Sync(self):
        sqlGet = f"SELECT COUNT(RA) FROM alunos WHERE RA = {self.RA}"
        oResultSet = self.db.execReadQuery(sqlGet)
        for x in oResultSet:
            if(x[0] > 0):
                update = f"UPDATE alunos SET nome = '{self.nome}', situacao = {self.situacao} WHERE RA = {self.RA}"
                self.db.execModQuery(update)
            else:
                insert = f"INSERT INTO alunos (RA, nome, situacao) VALUES ({self.RA}, '{self.nome}', {self.situacao})"
                self.db.execModQuery(insert)
        self.getAlunos()
    def getNext(self):
        sqlGet = "SELECT Max(RA) + 1 FROM alunos"
        oRS = self.db.execReadQuery(sqlGet)
        self.RA = oRS[0][0]
        self.nome = ""
        self.situacao = False
        return oRS[0][0]