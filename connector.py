import mysql.connector

def getMySQLConn() -> mysql.connector.connection.MySQLConnection:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="R@fael36",
        database="Faculdade"
    )
    return mydb
