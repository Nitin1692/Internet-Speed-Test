from tkinter import *
import speedtest

root = Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False,False)
root.configure(bg="#1a212d")

logo = PhotoImage(file="logo.png")
root.iconphoto(False,logo)

top = PhotoImage(file="top.png")
Label(root,image=top).pack()

Main = PhotoImage(file="main.png")
Label(root,image=Main).pack(pady=(40,0))

button = PhotoImage(file="Start.png")
Button = Button(root,image=button,bd=0,activebackground="#a1212d",cursor="hand2")
Button.pack(pady=20)

root.mainloop()