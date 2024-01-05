def ind():
    cur.execute('create database sm')
    cur.execute('use sm')
    cur.execute("""create table users (usna varchar(50) primary key,pas varchar(100) not null,naam varchar(50) not null,dob date not null,gen varchar(15) not null,con char(10) not null unique,bio varchar(500))""")
    #print('execution successful')

def che():
    cur.execute("show databases")
    t=[]
    for i in cur:
        t.append(str(i)[2:-3])
    #print(t)
    if 'sm' not in t:
        print('h')
        ind()



import mysql.connector as m
db=m.connect(host='localhost',user='root',password='system')
cur=db.cursor()
che()
