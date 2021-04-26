import socket
import threading

clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clisocket.connect(('localhost', 54321))
print('The client has been connected')

def RecvHandler():
    while True:
        print('The message from server.', clisocket.recv(256).decode())
threading._start_new_thread( RecvHandler,())

while True:
    msg = input('Please write the message :')
    clisocket.send(bytes(msg, encoding='utf8'))
