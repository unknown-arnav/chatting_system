def inp(t):
    pro=input(t)
    if pro[0:2]=="///":
        #keylaun(pro)
        return pro
    else:
        return pro
def keylaun(raw):
    keylist=['menu','keyword','b','home','','','','','','','','','','','','','','','','']
    if raw[3:] not in keylist:
        print('invalid keyword entered')
        print('try entering again')
        return
    elif raw[3:]=="menu":
        popme()
    elif raw[3:]=='keyword':
        pass#work in progess

def popme():
    print('Launching popup menu')
    print('PRESS--')
    print('1:to search for an user')
    print('2')

