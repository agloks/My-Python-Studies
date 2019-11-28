lista = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
#["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]

def moveZero(arr):
    count = 0
    index = 0
    falsos = []
    origin = arr.copy()
    for k in arr:
        if (k == 0):
            count += 1
        if (str(k) == 'False'):
            falsos.append(index)
        index += 1
    while(count > 0):
        arr.append(0)
        arr.remove(0)
        count -= 1
    for x in falsos:
        arr.insert(x-origin[:x].count(0),False)
        arr.reverse()
        arr.remove(0)
        arr.reverse()
    return arr

print ( moveZero(lista) )