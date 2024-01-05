def us(usna):
    cur.execute("use sm")
    cur.execute("select usna,naam from users")
    di={}
    l=set()
    for i,j in cur:
        di[str(j).lower()]=str(i).lower()
    #print(di)
    #sf=input('enter the name you want to search for:')
    sf='a'
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
        print(tmp)
        if usna!=[] and tmp[0]!=usna:
            c+=1
            udic[str(c)]=tmp[0].strip("'")
            print('USER:',c)
            print('USERNAME:',tmp[0])
            print('NAME:',tmp[1])
            print('GENDER:',tmp[2])
            print('BIO:',tmp[3])
            print('----------')




import mysql.connector as m
d=m.connect(host='localhost',user='root',password='system')
cur=d.cursor()
us('legendary_arnav')
