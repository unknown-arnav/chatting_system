#i bow to the entire lineage of my teachers
def smsg(u,r):
    print("(type ///e to stop texting and return to home)")
    ms=msg(u,r)
    while ms!="///e":
        ms=msg(u,r)
def msg(usna,rec):
    ms=inp(usna+':')
    if ms!="///e":
     cur.execute("use "+rec)
     cur.execute("insert into msg values('"+usna+"','"+ms+"',curdate(),curtime())")
     #print('success')
     cur.execute('commit')
     cur.execute("use "+usna)
    return ms


import mysql.connector as m 
mydb=m.connect(host='localhost',user='root',password='system')
cur=mydb.cursor()
from resources.key_check import *
usna="ar"
rec='a1'
#while True:
#    smsg(usna,rec)

