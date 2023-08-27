from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def shutdown():
    os.system("shutdown /s /t 1")

def logout():
    os.system("shutdown /l")

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Light Blue")

r_button = Button(st, text="Restart", font=("Verdana", 30, "bold"), relief=RAISED, command=restart)
r_button.place(x=150, y=60, height=60, width=250)

s_button = Button(st, text="Shutdown", font=("Verdana", 30, "bold"), relief=RAISED, command=shutdown)
s_button.place(x=150, y=170, height=60, width=250)

l_button = Button(st, text="Logout", font=("Verdana", 30, "bold"), relief=RAISED, command=logout)
l_button.place(x=150, y=270, height=60, width=250)

st.mainloop()