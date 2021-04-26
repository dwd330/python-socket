import socket
import threading
import tkinter as tk

#socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 54321))
print('The client has been connected')

def RecvHandler():
    while True:
        recive_label["text"] = 'recived message : ', s.recv(256).decode()
        

threading._start_new_thread( RecvHandler,())

#send message
def on_send():
     s.send(bytes(text_tosend.get("1.0",'end-1c'), encoding='utf-8'))

#gui
window = tk.Tk()
window.rowconfigure([0,1,2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
window.title("chat client")
window.geometry("800x600")
text_tosend= tk.Text(window, height = 10, width = 40 )
text_tosend.grid(row=0, column=1)
send_Button= tk.Button(window,width=30,height=5,bg="gray",fg="white", text ="send", command = on_send)
send_Button.grid(row=1, column=1)
recive_label= tk.Label(window,text ='recived..',font=("Arial", 25) )
recive_label.grid(row=2, column=1)
window.mainloop()






   
