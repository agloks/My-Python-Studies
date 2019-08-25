'''
1-fazer requisição para o site
2-pegar o resultado e salvar como arquivo "answer.json"
3-modificar o answer.json de acordo com o que for definido
4-envia o arquivo por via post para o mesmo site da requisição modificando o header

'''
import requests
import hashlib
import caesar
from . import caesar
import json
#example test use
'''
test={
	"numero_casas": 10,
	"token":"token_do_usuario",
	"cifrado": "texto criptografado",
	"decifrado": "aqui vai o texto decifrado",
	"resumo_criptografico": "aqui vai o resumo"
}
'''
#set site to requests
response = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=b197f3a0d3a183ac876c4d13b5ab295790c1509c")
date = response.json()
#function converting data in sha1
def sha1(data):
	return hashlib.sha1(str(data).encode()).hexdigest()

#function change content in file JSON
def change(data,*args):
	for x in args:
		data.update(x)

#variables need change
decifra = caesar.caesar(date.get('cifrado'),date.get('numero_casas'))
decifrado = {"decifrado":"{0}".format(decifra)}
resumir = sha1(decifra)
resumo = {"resumo_criptografico":"{0}".format(resumir)}


#take response and save on file answer.json
with open("answer.json","w") as f:
	change(date,decifrado,resumo)
	json.dump(date,f)
#with open("answer.json","w") as f:
#        obj = open("test.json","r")
#        txt = obj.read()
#        json.dump(txt,f)

#now, this part submit file to site
answer = {'answer':open("answer.json","rb")}

send = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=b197f3a0d3a183ac876c4d13b5ab295790c1509c',
                     files=answer)

print(send.status_code)
print(send.json())

