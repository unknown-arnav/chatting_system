def signup():
    ul=[]
    pl=[]
    cur.execute('use sm')
    cur.execute('select usna,con from users')
    for i,j in cur:
        ul.append(str(i)[2:-3])
        pl.append(str(j))
    while True:
        usna=input('enter the user name')
        if usna in ul :
            print('Sorry this username already exists')
            print('Please make an account with another username')
        elif len(usna)==0:
            print('Chutiya hai kya be')
            print('UserName cant be empty')
        elif len(usna)<8:
           print('USERNAME should be atleast 8 characters long')
        else:
            break
    while True:
        pas=input('enter the password')
        rep=input('re-enter the password')
        if pas==rep:
            break
        else:
            print('Error you have entered different password')
    na=input('enter your name')
    dob=input('enter your date of birth (YYYY-MM-DD)')
    se=input('enter your gender')
    while True:
        ph=input('enter phone number ')
        if ph not in pl:
            if len(ph)==10:
                break
            else:
                print("Invalid phone number entered")
        else:
            print('A user has already made an account with this phone number')
    bio=input('enter your desired bio')
    ln='insert into users values("'+usna+'","'+pas+'","'+na+'","'+dob+'","'+se+'","'+ph+'","'+bio+'")'
    cur.execute(ln)
    cur.execute('create database '+usna)
    cur.execute('use '+usna)
    cur.execute('create table msg (send_to varchar(50),msg varchar(500),date date,time time)')
    cur.execute('create table frnd (frnd varchar(50))')
    cur.execute('create table frndreq (frndreq varchar(50),waiting_frmd date,accepted char(2))')
    cur.execute('create table unrd (fro varchar(50))')
    print('SUCCESSFULLY CREATED YOUR ACCOUNT')
    print('Log into your account with the same creditals')
def login():
    up={}
    pp={}
    cur.execute('use sm')
    cur.execute('select usna,pas,con from users')
    for i,j,k in cur:
        up[str(i)]=str(j)
        pp[str(k)]=str(j)
    while True:
        us=input('enter username or phone number')
        tp=''
        for i in up:
            if i==us:
                tp=up[i]
        for j in pp:
            if i==us:
                tp=pp[j]
        if len(tp)==0:
            print("Sorry i couldn't find any account with such username or phone number")
            print("Please try checking typo errors")
        elif len(tp)!=0:
            break
    while True:
        ep=input('enter password')
        if tp!=ep:
            print('OHH! You have entered incorrect password')
            print('Please retry')
            print('enter ///b to try loging into another account')
        elif tp==ep:
            print('successfully logged in!!!')
            cur.execute('use '+us)
            break
        if ep=='///b':
            login()
            break
    return us
def logout():
    cur.execute('use sm')
    print('===================================================================')
    print('Successfully logged out')
    print('===================================================================')
    usna=''
    return usna




import mysql.connector as m
db=m.connect(host='localhost',user='root',password='system')
cur=db.cursor()
