#Creator Agl

a=[x for x in range(1,int(input())+1)]
while len(a) != 2:
        print(" "*4,"-->",a[0],"killed",a[1],"and given the sword to",a[2],"\n")
        del a[1]
        a.append(a[0])
        del(a[0])
        if(IndexError):
            pass

print("\n"," "*2,a[0],"Wins The Game Of Death Killing Last Alive",a[1])