#Creator Agl
a=input()
expopos=len(a)-1
exponeg=a.count('0')

def Findpos():
    c=list(a)
    c.reverse()
    counta=0
    while '0' in c[0]:
        counta+=1
        del c[0]
    valu=len(c)
    print (int(a)/10**expopos,'*','10','^',expopos)

def Findneg():
    c=list(a)
    counta=0
    countarev=0
    while '0' in c[0] or '.' in c[0]:
        counta+=1
        del c[0]
    print (float(a)*10**(counta-1),'*','10','^','-',counta-1)

while 1:
    if a[0]=='0':
        Findneg()
        break
    elif a[0]!='0':
        Findpos()
        break