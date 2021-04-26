import socket
import threading

srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server socket opened')

srvsocket.bind(('localhost', 54321))
print('Bind to the local port')

srvsocket.listen(5)
print('Started listening...')

#New Client Recive Handler
def NewClientRecvHandler(cli,):
    print('The new client has socket id:', cli)
    while True:
        print('The message got for client socket:', cli)
        print(cli.recv(256).decode())

#New Client send Handler
def NewClientSendHandler(cli,):
    print('The new client has socket id:', cli)
    while True:
        inputdata=input('data to send:')
        print('The message sent to client socket:', cli)
        cli.send(bytes('sending:'+inputdata, encoding='utf8'))

while True:
    print('Waiting for the incoming connections..')
    cli, ip = srvsocket.accept()
    cli.send(bytes('CONNECT_SUCCESSFUL', encoding='utf8'))

    #Start the new client thread
    threading._start_new_thread( NewClientRecvHandler, (cli,))
    threading._start_new_thread( NewClientSendHandler, (cli,))
    
