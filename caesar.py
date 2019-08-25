#Creator Agl
import string

def caesar(entrada,number):
        text = ''
        for x in entrada:
                if x in string.ascii_lowercase:
                        text+=chr(ord(x)-number) if ord(x)-number>=97 else chr(122-abs((97-ord(x)))) if ord(x)-abs((97-ord(x)))!=97 else chr(123-(abs(97-ord(x)))) if x != 'a' else chr(123-number)
                else:
                        text+=x
        return text

'''
def caesar(entrada):
        wordsnum={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'
                  ,10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',
                  18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z',
                  26:' '}
        addaq=[]
        agora=list(entrada)
        numb=[]
        encry=[]
        counta=0
        while addaq != agora:
                for ko in wordsnum:
                        if agora[counta] in wordsnum[ko]:
                                counta+=1
                                numb.append(ko)
                                addaq.append(wordsnum[ko])
                                break
        for numba in numb:
                try:
                        if numba == 26:
                                encry.append(wordsnum[numba])
                        else:
                                encry.append(wordsnum[numba+3])
                except KeyError:
                        if numba == 26:
                                encry.append(wordsnum[numba])
                        else:
                                encry.append(wordsnum[(numba+3)-numba])
        result = "".join(encry)
        return result
'''
if __name__=="__main__":

        entrada=input("Escreva o texto:\n")
        number=int(input("Qual numero da cifra:\n"))
        print(caesar(entrada,number))
