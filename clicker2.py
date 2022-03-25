
import tkinter as tk
from tkinter import * 
import random

count = 0
window = tk.Tk()
window.geometry("500x400")
window.title('Clicker')
window.configure(bg='gray')
countUp = tk.IntVar(0)

def on_enter(e):
   window.configure(bg="yellow")

def on_leave(e):
    if countUp.get() >=1:
        window.configure(bg="green")
    elif countUp.get() <= -1:
        window.configure(bg="red")
    else:
        window.configure(bg="gray")


def button_pressed_1():
    global count
    count += 1
    countUp.set(count)
    if countUp.get() >= 1:
        window.configure(bg="green")
    elif countUp.get() <= -1:
        window.configure(bg="red")
    else:
        window.configure(bg="gray")


def button_pressed_2():
    global count
    count -= 1
    countUp.set(count)
    if countUp.get() >= 1:
        window.configure(bg="green")
    elif countUp.get() <= -1:
        window.configure(bg="red")
    else:
        window.configure(bg="gray")

button_1 = Button(window,text = "Up", command=button_pressed_1)
button_1.config(height=5,width=30)

button_2 = Button(window,text = "Down", command=button_pressed_2)
button_2.config(height=5,width=30)

label_count = tk.Label(window, text=count)
label_count.config(height=5,width=30,textvariable=countUp,activebackground="Yellow")

button_1.pack()
button_2.pack(side= BOTTOM)
label_count.place(x=250, y=200, anchor="center")

label_count.bind('<Enter>', on_enter)
label_count.bind('<Leave>', on_leave)

window.mainloop()