from csv import DictReader, reader
from math import dist
from os import curdir
from turtle import update
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    password="admin",
    database="testdb"
)


def Create():
    q = 'create table if not exists user(userId int primary key, userName varchar(20), phone varchar(12))'
    cur = mydb.cursor()
    cur.execute(q)
    # print(cur)


def Inserting():
    q = 'insert into user values(1283,"Kawser",017312)'
    cur = mydb.cursor()
    cur.execute(q)
    mydb.commit()


def showDb():
    q = 'select * from user'
    cur = mydb.cursor()
    cur.execute(q)
    for line in cur:
        print(line)


def updateDb(id, name):
    q = "UPDATE user SET userName = %s WHERE userId = %s"  # SQL Injection
    val = (name, id)
    cur = mydb.cursor()
    cur.execute(q, val)
    mydb.commit()


def delete(name):
    mycursor = mydb.cursor()
    sql = "DELETE FROM user WHERE userName ='{}'".format(name)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")


