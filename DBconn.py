import mysql.connector
import sqlite3
conn= sqlite3.connect("example.db")
cursor=conn.cursor()
#cursor.execute("""create Table student (Roll int primary key, name Text ,age int  )""")
#conn.close()


users=[]
for roll in range(4, 20):
    user=(roll,f"user{roll}",roll+5)
    users.append(user)
users


with sqlite3.connect("example.db") as conn:
    #cursor=conn.curser()
    cursor.executemany(
        """Insert Into student VALUES (?,?,?)""",users
        
        
    )




with sqlite3.connect("example.db") as conn:
    #cursor=conn.curser()
    Result=cursor.execute(
      """SELECT * From student"""
        
    )  

    print(list(Result)) 
with sqlite3.connect("example.db") as conn:
    #cursor=conn.curser()
    Result=cursor.execute(
      """SELECT name,age From student where age<15"""
        
    )  

    print(list(Result)) 