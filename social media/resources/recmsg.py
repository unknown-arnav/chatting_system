#i bow to the entire lineage of my teachers
#from key_check import *
def loadchat(usna,fro):
    import time
    print('loading chats:PLEASE WAIT')
    time.sleep(2)
    o=[]
    cur.execute("use "+fro)
    cur.execute("select * from msg where send_to='"+usna+"' order by date desc,time desc")
    for i in cur :
        tmp=[]
        t2=str(i)[2:-3].split(',')
        us=t2[0][:-1]
        tmp.append(us)
        ms=t2[1][2:-1]
        tmp.append(ms)
        da=t2[2][-4:]+'-'+t2[3]+'-'+t2[4][:-1]
        tmp.append(da)
        ti=t2[5][-4:]
        tmp.append(ti)
        #print(tmp)
        o.append(tmp)
    cur.execute("use "+usna)
    cur.execute("select * from msg where send_to='"+fro+"' order by date desc,time desc")
    s=[]
    for i in cur :
        tmp=[]
        t2=str(i)[2:-3].split(',')
        us=t2[0][:-1]
        tmp.append(us)
        ms=t2[1][2:-1]
        tmp.append(ms)
        da=t2[2][-4:]+'-'+t2[3]+'-'+t2[4][:-1]
        tmp.append(da)
        ti=t2[5][-4:]
        tmp.append(ti)
        #print(tmp)
        s.append(tmp)
    #printing the chatsXOXO
    if len(o)==0 and len(s)==0:
        print('YOU ARE CHATING FOR THE FIRST TIME WITH THE USER')
    u1=[]
    u2=[]
    for i in range (len(o)+len(s)):
        if u1==[]:
            try:
                u1=o.pop()
            except:
                u1=['','','2000-01-01','000']
        if u2==[]:
            try:
                u2=s.pop()
            except:
                u2=['','','2000-01-01','000']
        if u1[2]<u2[2]:
            if u1[0]!='':
                print(u1[0]+':'+u1[1])
                u1=[]
            else:
                print(u2[0]+':'+u2[1])
                u2=[]
        elif u1[2]>u2[2]:
            if u2[0]!='':
                print(u2[0]+':'+u2[1])
                u2=[]
            else:
                print(u1[0]+':'+u1[1])
                u1=[]
        else:
            if u1[3]<u2[3]:
                if u1[0]!='':
                    print(u1[0]+':'+u1[1])
                    u1=[]
                else:
                    print(u2[0]+':'+u2[1])
                    u2=[]
            elif u1[3]>u2[3]:
                if u2[0]!='':
                    print(u2[0]+':'+u2[1])
                    u2=[]
                else:
                    print(u1[0]+':'+u1[1])
                    u1=[]
    #print (u1)
    #print(u2)
    


import mysql.connector as m
db=m.connect(host='localhost',user='root',password='system')
cur=db.cursor()
usna='ar'
chop='a1'
#loadchat(usna,chop)

