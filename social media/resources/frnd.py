#i bow to the entire lineage of my teachers
def make(usna,fro):
    cur.execute("use "+usna)
    cur.execute("select * from frnd")
    tp=[]
    for i in cur:
        tp.append(str(i)[2:-3])
    if usna not in tp:
        cur.execute('use '+fro)
        cur.execute("delete from frndreq where frndreq='"+usna+"'")
        cur.execute("insert into frndreq(frndreq,waiting_frmd) values('"+usna+"',curdate())")
        cur.execute("commit")
        print("success")
    else:
        print(fro+" is already your friend")
def accept(usna,fro):
    cur.execute("use "+fro)
    cur.execute("insert into frnd values('"+usna+"')")
    cur.execute("use "+usna)
    cur.execute("insert into frnd values('"+fro+"')")
    cur.execute("delete from frndreq where frndreq='"+fro+"'")
    cur.execute("commit")
    print('SUCCESS')
    pass
def disreq(usna):
    cur.execute('use '+usna)
    cur.execute("select*from frndreq")
    a=[]
    for i in cur:
        a.append(str(i)[2:-37])
    #print(a)
    c=0
    udic={}
    for i in a:
        cur.execute("use sm")
        cur.execute("select usna,naam,gen,bio from users where usna='"+str(i)+"'")
        tmp=[]
        tmpt=""
        for l in cur:
            tmpt=str(l)[1:-1]
            tmp=tmpt.split(',')
        if tmp[0]!=usna:
            c+=1
            udic[str(c)]=tmp[0].strip("'")
            print('USER:',c)
            print('USERNAME:',tmp[0])
            print('NAME:',tmp[1])
            print('GENDER:',tmp[2])
            print('BIO:',tmp[3])
            print('----------')
    if c==0:
        print("YOU HAVE NO FRIEND REQUESTS")
    else:
        while True:
            usc=selection(udic,"enter the username or user number to accept its request")
            co=inp("Are you sure that you want to accept the request of"+usc+"?(y/n)")
            if co.lower()[0]=='y':
                break
        #print('loop se bahar aa gya')
        accept(usna,usc)











from resources.user_search import *
import mysql.connector as m
mydb=m.connect(host='localhost',user='root',password='system')
cur=mydb.cursor()
#make('a1','ar')
#disreq('ar')
