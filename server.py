import threading
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server socket opened')

s.bind(('localhost', 54321))
print('Bind to the local port')

s.listen(5)
print('Started listening...')
clients=[]
#New user connect Handler
def connectnewuser(c,ad):
    while True:
        print('The message got for client socket:', c)
        m=c.recv(256).decode()
        m=(ad[0]+':'+m)
        sendtoall(m,c)
def sendtoall(m,c):
    for client in clients:
        if client !=c:
            client.send(m.encode('utf-8'))
while True:
    c,ad=s.accept()
    clients.append(c)
    threading._start_new_thread(connectnewuser,(c,ad))


