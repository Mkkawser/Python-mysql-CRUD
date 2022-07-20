import mysql.connector


class MyDB:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost", user="root", password="admin", database="testdb"
        )

    def showDB(self):
        cur = self.con.cursor()
        cur.execute("show databases")
        for line in cur:
            print(line)

    def createDB(self):
        q = 'create database if not exists testdb'
        cur = self.con.cursor()
        cur.execute(q)

    def createTable(self):
        q = 'create table if not exists user(id int primary key,name varchar(55),phone varchar(55))'
        cur = self.con.cursor()
        cur.execute(q)
        self.con.commit()

    def insert(self, id, name, phone):
        q = 'insert into user values(%s,%s,%s)'
        val = (id, name, phone)
        cur = self.con.cursor()
        cur.execute(q, val)
        self.con.commit()

    def updateDB(self, i, n, p):
        q = 'update user set name=%s ,phone=%s where id=%s'
        val = (n, p, i)
        cur = self.con.cursor()
        cur.execute(q, val)
        self.con.commit()

    def deleteDB(self, i):
        q = 'delete from user where id=%s'
        val = (i,)
        cur = self.con.cursor()
        cur.execute(q, val)
        self.con.commit()


DB_ = MyDB()
# DB_.createDB()
# DB_.showDB()
# DB_.createTable()
# DB_.insert(1285, "MK", "0173")
# DB_.updateDB(1283, "Kawser", "016311")
# DB_.deleteDB(1283)
