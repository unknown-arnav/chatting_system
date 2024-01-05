#Before fighting a war, One has to win the war from SELF
from resources.key_check import *
def usear(usna):
    print('Launching user searching')
    cur.execute("use sm")
    cur.execute("select usna,naam from users")
    di={}
    l=set()
    for i,j in cur:
        di[str(j).lower()]=str(i).lower()
    #print(di)
    sf=inp('enter the name you want to search for:')
    sf=sf.lower()
    c=0
    udic={}
    nl=list(di.keys())
    ul=list(di.values())
    na=nl[ul.index(usna)]
    #print(na)
    for i in ul:
        if sf in i and i!=usna.lower():
            l.add(i)
    for j in nl:
        if sf in j and j!=na.lower():
            l.add(di[j])
    print(l)
    for i in l:
        cur.execute("select usna,naam,gen,bio from users where usna='"+i+"'")
        tmp=[]
        tmpt=""
        for l in cur:
            tmpt=str(l)[1:-1]
            tmp=tmpt.split(',')
        #print(tmp)
        if usna!=[] and tmp[0]!=usna:
            c+=1
            udic[str(c)]=tmp[0].strip("'")
            print('USER:',c)
            print('USERNAME:',tmp[0])
            print('NAME:',tmp[1])
            print('GENDER:',tmp[2])
            print('BIO:',tmp[3])
            print('----------')
    if c!=0:    
        pass
    elif c==0:
        print('NO USER FOUND')
        print('----------')
    while True:
        usc=selection(udic,"enter the username or user number to select the user")
        con=inp('Are you sure that you want to select '+usc+'?(y/n)')
        if con.lower()[0]=='y':
            return usc
            break

def usearch(usna):
    cur.execute("use "+usna)
    cur.execute("select*from frnd")
    l=[]
    c=0
    udic={}
    for i in cur:
        l.append(str(i)[2:-3])
    #print(l)
    for i in l:
        cur.execute("use sm")
        cur.execute("select usna,naam,gen,bio from users where usna='"+str(i)+"'")
        tmp=[]
        tmpt=""
        for l in cur:
            tmpt=str(l)[1:-1]
            tmp=tmpt.split(',')
        c+=1
        #print(tmp)
        udic[str(c)]=tmp[0].strip("'")
        print('USER:',c)
        print('USERNAME:',tmp[0])
        print('NAME:',tmp[1])
        print('GENDER:',tmp[2])
        print('BIO:',tmp[3])
        print('----------')
    if c==0:
        print("YOU HAVE NO FRIENDS TO MESSAGE")
        print('YOU CAN MAKE FRIENDS BY REQUESTING THEM IN THE MAKIG NEW FRIENDS DESCTION ON THE HOME')
    else:
        while True:
            usc=selection(udic,"enter the username or user number to message them")
            co=inp("Are you sure that you want to message "+usc+"?(y/n)")
            if co.lower()[0]=='y':
                break
        #print('loop se bahar aa gya')
        return usc










def selection(udic,t):
    usl=list(udic.values())
    unl=list(udic.keys())
    #print(usl,unl)
    f=0
    while True:
        usc=inp(t)
        for i in usl:
            if usc==i:
                f=1
                break
        for i in unl :
            if usc==i:
                f=2
                break
        if f==0:
            print('INVALID USER')
        elif f==1 or f==2:
            break
    if f==2:
        usc=udic[usc]
    return usc






    
#main
import mysql.connector as m
db=m.connect(host='localhost',user='root',password='system')
cur=db.cursor()
#print(usearch('legendary_arnav'))
#usearch('a1')
