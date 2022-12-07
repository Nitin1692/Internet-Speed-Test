from tkinter import *
import speedtest
import threading

root = Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False,False)
root.configure(bg="#1a212d")

def Check():
    test = speedtest.Speedtest()

    Uploading = round(test.upload()/(1024*1024),2)
    upload.config(text=Uploading)

    downloading = round(test.download()/(1024*1024),2)
    download.config(text=downloading)
    Download.config(text=downloading)
    
    servernames= []
    test.get_servers(servernames)
    ping.config(text=test.results.ping)

logo = PhotoImage(file="logo.png")
root.iconphoto(False,logo)

top = PhotoImage(file="top.png")
Label(root,image=top).pack()

Main = PhotoImage(file="main.png")
Label(root,image=Main).pack(pady=(40,0))

button = PhotoImage(file="Start.png")
Button = Button(root,image=button,bd=0,activebackground="#a1212d",cursor="hand2",command=threading.Thread(target=Check).start())
Button.pack(pady=20)

Label(root,text="PING",font="arial 10 bold",bg="#949494").place(x=45,y=100)
Label(root,text="DOWNLOAD",font="arial 10 bold",bg="#949494").place(x=135,y=100)
Label(root,text="UPLOAD",font="arial 10 bold",bg="#949494").place(x=260,y=100)

Label(root,text="MS",font="arial 7 bold",bg="#949494",fg="black").place(x=55,y=75)
Label(root,text="MBPS",font="arial 7 bold",bg="#949494",fg="black").place(x=160,y=75)
Label(root,text="MBPS",font="arial 7 bold",bg="#949494",fg="black").place(x=270,y=75)

Label(root,text="Download",font="arial 15 bold",bg="#949494",fg="black").place(x=130,y=300)
Label(root,text="MBPS",font="arial 15 bold",bg="#949494",fg="black").place(x=151,y=390)

ping = Label(root,text="00",font="arial 13 bold",bg="#949494",fg="black")
ping.place(x=65,y=60,anchor="center")

download = Label(root,text="00",font="arial 13 bold",bg="#949494",fg="black")
download.place(x=175,y=60,anchor="center")

upload = Label(root,text="00",font="arial 13 bold",bg="#949494",fg="black")
upload.place(x=285,y=60,anchor="center")

Download = Label(root,text="00",font="arial 40 bold",bg="#949494")
Download.place(x=185,y=360,anchor="center")

root.mainloop()