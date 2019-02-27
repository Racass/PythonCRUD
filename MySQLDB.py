import mysql.connector
import connector

class mySQL:
    myDB = connector.getMySQLConn()
    autoCommit = True
    def execModQuery(self, query: str) -> int:
        myCursor = self.myDB.cursor()
        myCursor.execute(query)
        if(self.autoCommit):
            self.myDB.commit()
        return myCursor.rowcount
    def execReadQuery(self, query: str):
        myCursor = self.myDB.cursor()
        myCursor.execute(query)
        return myCursor.fetchall()
    def commit(self):
        self.myDB.commit()