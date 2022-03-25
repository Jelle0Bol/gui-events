
import tkinter as tk
from tkinter import * 

count = 0
window = tk.Tk()
window.geometry("500x400")
window.title('Clicker V.4')
window.configure(bg='gray')
countUp = tk.IntVar(0)
double_button_pressed = False



    

def on_enter(e):
   window.configure(bg="yellow")

def on_leave(e):
    if countUp.get() >=1:
        window.configure(bg="green")
    elif countUp.get() <= -1:
        window.configure(bg="red")
    else:
        window.configure(bg="gray")


def button_pressed_1(self):
    global count, button_triple
    button_triple = "omhoog"
    which_button()
    count += 1
    countUp.set(count)
    if countUp.get() >= 1:
        window.configure(bg="green")
    elif countUp.get() <= -1:
        window.configure(bg="red")
    else:
        window.configure(bg="gray")


def button_pressed_2(self):
    global count, button_triple
    button_triple = "omlaag"
    which_button()
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

def button_pressed_3(self):
    global double_button_pressed
    double_button_pressed = True

button_1.bind('<Double-Button-1>', button_pressed_3)
button_2.bind('<Double-Button-1>', button_pressed_3)

def which_button():
    global button_triple, count, double_button_pressed
    if button_triple == "omhoog" and double_button_pressed == True:
        count *= 3
        count -= 4
        double_button_pressed = False
    elif button_triple == "omlaag" and double_button_pressed == True:
        count /= 3
        count = int(count)
        count += 4
        count -= 2 
        double_button_pressed = False

def button_pressed_4(self):
    global button_triple, count, double_button_pressed
    if button_triple == "omhoog":
        count *= 3
        countUp.set(count)
    elif button_triple == "omlaag":
        count /= 3
        count = int(count)
        countUp.set(count)
    else:
        print("Fout")







button_1.pack()
button_2.pack(side= BOTTOM)
label_count.place(x=250, y=200, anchor="center")

label_count.bind('<Enter>', on_enter)
label_count.bind('<Leave>', on_leave)
window.bind("<Up>", button_pressed_1 )
window.bind("+", button_pressed_1 )
window.bind("<Down>", button_pressed_2 )
window.bind("-", button_pressed_2 )
window.bind("<space>",button_pressed_4)

window.mainloop()