#i bow to the entire lineage of my teachers
def mod(usna):
    cur.execute("use sm")
    cur.execute("select*from users where usna='"+usna+"'")
    for i in cur:
        l=str(i).split(',')
    print(l)
    print("YOUR ACCOUNT LOOKS LIKE:")
    print('1'+')USERNAME:',l[0][2:-1])
    print('2'+')PASSWORD:',l[1][2:-1])
    print('3'+')NAME:',l[2][2:-1])
    print('4'+')DOB:',l[3][-4:]+'-'+l[4][1:]+'-'+l[5][1:-1])
    print('5'+')GENDER:',l[6][2:-1])
    print('6'+')CONTACT NO.:',l[7][2:-1])
    print('7'+')BIO:',l[8][2:-2])
    print('8)FRIENDS LIST')
    while True:
        c=inp("Select the number corresponding to the option you want to modify:")
        if c=='1':
            print("YOU CAN'T CHANGE YOUR USERNAME AT LEAST FOR NOW")
        elif c=='2':
            while True:
                np=inp('Enter new password')
                if np==l[1][2:-1]:
                    print("You can't enter your previous password")
                else:
                    cur.execute("use sm")
                    cur.execute("update users set pas='"+np+"'where usna='"+usna+"'")
                    print("SUCCESSFULLY CHANGED YOUR PASSWORD")
                    cur.execute('commit')
                    break
            break
        elif c=='3':
            while True:
                np=inp('Enter new name')
                if np==l[2][2:-1]:
                    print("You can't enter your previous name")
                else:
                    cur.execute("use sm")
                    cur.execute("update users set naam='"+np+"'where usna='"+usna+"'")
                    print("SUCCESSFULLY CHANGED YOUR NAME")
                    cur.execute('commit')
                    break
            break
        elif c=='4':
            while True:
                np=inp('Enter new dob(yyyy-mm-dd)')
                if np==l[3][-4:]+'-'+l[4][1:]+'-'+l[5][1:-1]:
                    print("You can't enter your previous dob")
                else:
                    cur.execute("use sm")
                    cur.execute("update users set dob='"+np+"'where usna='"+usna+"'")
                    print("SUCCESSFULLY CHANGED YOUR DOB")
                    cur.execute('commit')
                    break
            break
        elif c=='5':
            print("YOU CAN'T CHANGE YOUR GENDER")
        elif c=='6':
            while true:
                np=inp('Enter new phone number')
                if np==l[7][2:-1]:
                    print("You can't enter your previous contact number")
                else:
                    cur.execute("use sm")
                    cur.execute("update users set con='"+np+"'where usna='"+usna+"'")
                    print("SUCCESSFULLY CHANGED YOUR CONTACT")
                    cur.execute('commit')
                    break
            break
        elif c=='7':
            while True:
                np=inp('Enter new bio')
                if np==l[8][2:-2]:
                    print("You can't enter your previous bio")
                else:
                    cur.execute("use sm")
                    cur.execute("update users set bio='"+np+"'where usna='"+usna+"'")
                    print("SUCCESSFULLY CHANGED YOUR PASSWORD")
                    cur.execute('commit')
                    break
            break
        elif c=="8":
            li=[]
            cur.execute("use "+usna)
            cur.execute("select*from frnd")
            for i in cur:
                li.append(str(i)[2:-3])
            #print(li)
            c=0
            udic={}
            for i in li:
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
                print("YOU HAVE NO FRIEND REQUESTS")
            else:
                s=inp('Do you want to remove any user from your friends list?(y/n)')
                if s.lower()[0]=='y':
                    while True:
                        usc=sel(udic,"enter the username or user number to remove from your friends list")
                        co=inp("Are you sure that you want to accept the request of "+usc+"?(y/n)")
                        if co.lower()[0]=='y':
                            break
                    #print('loop se bahar aa gya')done till here
                    cur.execute('use '+usna)
                    cur.execute("delete from frnd where frnd='"+usc+"'")
                    cur.execute('commit')
                    cur.execute("use "+usc)
                    cur.execute("delete from frnd where frnd='"+usna+"'")
                    cur.execute('commit')
                    print("SUCCESSFULLY REMOVED THE USER",usc,"FROM YOUR FRIENDS LIST")
        elif c=='///e':
            break
        else:
            print("INVALID OPTION SELECTED")
            print("PLEASE TRY AGAIN. ENTER INTEGER BETWEEN 1 TO 8")
        print('You an return to home screen by typing ///e')
def sel(udic,t):
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




from resources.key_check import *
from resources.user_search import *
import mysql.connector as m
db=m.connect(host='localhost',user='root',password='system')
cur=db.cursor()
#mod('a1')
#print('h')
