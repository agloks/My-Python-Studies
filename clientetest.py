#!python3.5
import socket,sys

socket_exit = "exit"
msg = input()

host = ""
port = 57845

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

on = True

while on:
	msg = input()
	s.send(str.encode(msg))
	data = s.recv(1024)
	if(msg == "exit"):
		s.close()
		on = False
		sys.exit()
	print("Recebi de data do servidor:\n",data.decode('utf-8'),"\n")
