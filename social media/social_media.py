from resources.sm import *
from resources.msger import *
from resources.recmsg import *
from resources.sign_options import *
from resources.user_search import *
from resources.key_check import *
from resources.frnd import *
from resources.index import *
from resources.modi import *
import mysql.connector as m 
db=m.connect(host='localhost' ,user='root' ,password='system')
cur=db.cursor()
ul=[]
pl=[]
cur.execute('use sm')
cur.execute('select usna,con from users')
for i,j in cur:
    ul.append(str(i)[2:-3])
    pl.append(str(j))
while True:
    while True:
        print('==============================================================================')
        print('----------------------------------------WELCOME-------------------------------')
        print('please select one of the following operations')
        print('==============================================================================')
        print('1: To create a new account')
        print('2:To login into an existing account')
        c=int(input ())
        print('==============================================================================')
        if c==1:
            signup()
            usna=login()
            break
        elif c==2:
            usna=login()
            break
        else:
            print('INVALID value entered')
    while True:
        mainintro()
        print("=====================HOME=======================")
        c=int(inp('enter any operation(1-5)'))
        if c==1:
            #messaging
            fro=usearch(usna)
            #print(usna,fro)
            loadchat(usna,fro)
            smsg(usna,fro)
        elif c==2:
            #sending_frnd_request
            fro=usear(usna)
            make(usna,fro)
        elif c==3:
            #frnd_req
            disreq(usna)
        elif c==4:
             #pro_modi
             mod(usna)
        elif c==5:
            usna=logout()
            break
        else:
            print('ERROR!!!!!Invalid operation selected')
            mainintro()
            print('please enter valid opertor')
        







