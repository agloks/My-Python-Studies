from itertools import permutations

class Search():
    #As variaveis globais e iniciais que necessitam posteriomente
    def __init__(self,file,txt,qnt):
        self.txt = txt
        self.qnt = int(qnt)
        self.file = file
        self.result = []
    #Função que verificar cada item de x e ver se encontra no arquivo op
    def Match(self,txt):
        #abrir arquivo
        op = open(r"{}".format(self.file)).read()
        #lista comprimida das permutations
        x = ["".join(x) for x in list(permutations(txt))]
        #pega cada item em x e ver se ta em op, se tiver retorna-o
        for b in x:
            if b in op:
                return b
    #função recursiva que chama Search e opera um item por cada vez e retorna na variavel self.result
    def Result(self):
        for x in range(1):
            self.result.append("".join(list(map(self.Match,self.txt.split()))))
        return self.result

#Começo do Programa
if __name__ == "__main__":
    print("Script executed,but don't the functions why it's module\n")
    on = True
    while on:
        new = input("To exit press q, to go press any tecle on keyboard... ")
        if new == 'q' or new == 'Q':
            on = False
        else:
            file = input("Write path for file -->\n")
            qnt=int(input("Now,How many need:  \n"))
            txt=''
            oficial=[]
            print("Then end,Write all words:")
            for x in range(qnt):
                try:
                    txt=input()
                    a=Search(file,txt,qnt)
                    oficial.append(''.join(a.Result()))
                except(TypeError):
                    pass
            print('\n',','.join(oficial))
