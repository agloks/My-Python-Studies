#Agl

'''Enter with an integer'''

l=""
a=lambda x,j:[[str(d) for d in range(1,x+1)if j%d==0],[b for b in range(1,j+1)if j%b==0]]
for k in range(2,int(input())+1):
    exec(f"\nc=1\nfor i in range(len(a({k},{k})[0])):\n\tc*=a({k},{k})[1][i]\n\tif c==k**3:\n\t\tl+=\"{k} => {k}**3 == \"+\"*\".join(a({k},{k})[0])+\" == \"+str(c)+\"\\n\\n\"")
    
print("\t"*6,"All Fisher Number On Range Given","\n"*3+l,"\n"+"-"*50+"\n"*2,[str(k)+" is fisher number because "+str(k)+"**3 == "+"*".join(a(k,k)[0])][0]if str(k) in l.split() else [str(k)+" isn't fisher number because "+str(k)+"**3 != "+"*".join(a(k,k)[0])][0])