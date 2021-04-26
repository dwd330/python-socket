import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 54321))
print('The client has been connected')

def RecvHandler():
    while True:
        print('The message from server.', s.recv(256).decode())
threading._start_new_thread( RecvHandler,())

while True:
    msg = input('Please write the message :')
    s.send(bytes(msg, encoding='utf8'))
