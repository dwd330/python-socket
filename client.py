import socket
import threading
from  tkinter import * 
index=0
#socket create
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 54321))

#handle recive
def RecvHandler():
    while True:
        global index
        recived=s.recv(256).decode()
        msg_list.insert(index,recived)
        index+=1
        
threading._start_new_thread( RecvHandler,())

#send message
def on_send():
     global index
     msg_send=text_tosend.get("1.0",'end-1c')
     msg_list.insert(index,msg_send)
     index+=1
     s.send(bytes(msg_send, encoding='utf-8'))
     text_tosend.delete('1.0', END)


#gui
window = Tk()
window.rowconfigure([0,1,2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
window.title("chat client")
window.geometry("800x600")
# create listbox object
msg_list = Listbox(window, height = 30, 
                  width = 40, 
                  bg = "white",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "blue")
msg_list.grid(row=0, column=1)
      
text_tosend= Text(window, height = 10, width = 40 )
text_tosend.grid(row=2, column=1)
send_Button= Button(window,width=30,height=5,bg="gray",fg="white", text ="send", command = on_send)
send_Button.grid(row=2, column=2)
recive_label= Label(window,text ='recived..',font=("Arial", 25) )
window.mainloop()






   
