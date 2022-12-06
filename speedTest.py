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

root.mainloop()