#!/usr/local/bin/python3

import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk

a = -1
b = -1
right = 0
wrong = 0
maxim_good = 10
maxim_bad = 1
maxim = 100
photo_path = "photo/"
to_do = 0
sec= 0

def init():
    global right
    global wrong
    global to_do
    global sec
    right = 0
    wrong = 0
    to_do = 1
    sec = 0
    new_game()

def h_new_game(event):
    init()

def h_exit(event):
    exit_game()

def h_is_small(event):
    if to_do: is_small()

def h_is_eq(event):
    if to_do: is_eq()

def h_is_big(event):
    if to_do: is_big()

def new_game():
    global a
    global b
    global right
    global wrong
    global status
    global maxim_good
    global maxim_bad
    global to_do
    if right == maxim_good:
        img_status = ImageTk.PhotoImage(Image.open(photo_path + "bravo_matei.jpg"))
        label_status.config(image=img_status)
        label_status.image = img_status
        to_do = 0        
    elif wrong == maxim_bad:
        img_status = ImageTk.PhotoImage(Image.open(photo_path + "game_over.jpg"))
        label_status.config(image=img_status)
        label_status.image = img_status
        to_do = 0        
    else: 
        a = random.randint(0, maxim)
        b = random.randint(0, maxim)
        label_top_a1.config(text=str(a))
        label_top_c1.config(text=str(b))
        img_status = ImageTk.PhotoImage(Image.open(photo_path + "hai_matei.jpg"))
        label_status.config(image=img_status)
        label_status.image = img_status
    label_right_c3.config(text=str(right) + " / " + str(maxim_good))

def exit_game():
	root.destroy()

def is_big():
    global a
    global b
    global right
    global wrong
    if a > b:
        right += 1
    else:
        wrong += 1
    new_game()

def is_eq():
    global a
    global b
    global right
    global wrong
    if a == b:
        right += 1
    else:
        wrong += 1
    new_game()

def is_small():
    global a
    global b
    global right
    global wrong
    if a < b:
        right += 1
    else:
        wrong += 1
    new_game()

def update_timer():
    global sec
    global to_do
    if to_do:
        sec += 1
        label_timer.config(text=str(sec))
    root.after(1000, update_timer)


root = tk.Tk()
root.title("...MAT_0...")
root.geometry("500x500")
root.resizable(0, 0)

img_bg = ImageTk.PhotoImage(Image.open(photo_path + "fundal.jpg"))
label_bg = tk.Label(root, image=img_bg)
label_bg.place(relx=0, rely=0, relwidth=1, relheight=1)

label_top_a1 = tk.Label(root, text="A", foreground="white", background="black", font=("Helvetica", 32))
label_top_a1.place(x=0, y=0, width=100, height=100)
label_top_c1 = tk.Label(root, text="B", foreground="white", background="black", font=("Helvetica", 32))
label_top_c1.place(x=200, y=0, width=100, height=100)

img_small = ImageTk.PhotoImage(Image.open(photo_path + "mai_mic.jpg"))
label_small = tk.Label(root, image=img_small)
label_small.place(x=0, y=100, width=100, height=100)
label_small.bind("<Button-1>", h_is_small)

img_eq = ImageTk.PhotoImage(Image.open(photo_path + "egal.jpg"))
label_eq = tk.Label(root, image=img_eq)
label_eq.place(x=100, y=100, width=100, height=100)
label_eq.bind("<Button-1>", h_is_eq)

img_big = ImageTk.PhotoImage(Image.open(photo_path + "mai_mare.jpg"))
label_big = tk.Label(root, image=img_big)
label_big.place(x=200, y=100, width=100, height=100)
label_big.bind("<Button-1>", h_is_big)

label_right_c3 = tk.Label(root, text=str(right) + " / " + str(maxim_good), 
    foreground="white", background="black", font=("Helvetica", 32))
label_right_c3.place(x=300, y=400, width=200, height=100)

label_timer = tk.Label(root, text=str(sec), foreground="white", background="black", font=("Helvetica", 32))
label_timer.place(x=300, y=300, width=200, height=100)

img_status = ImageTk.PhotoImage(Image.open(photo_path + "hai_matei.jpg"))
label_status = tk.Label(root, image=img_status)
label_status.place(x=0, y=200, width=300, height=100)

img_new_game = ImageTk.PhotoImage(Image.open(photo_path + "new_game.jpg"))
label_new_game = tk.Label(root, image=img_new_game)
label_new_game.place(x=0, y=300, width=150, height=100)
label_new_game.bind("<Button-1>", h_new_game)

img_exit = ImageTk.PhotoImage(Image.open(photo_path + "exit.jpg"))
label_exit = tk.Label(root, image=img_exit)
label_exit.place(x=150, y=300, width=150, height=100)
label_exit.bind("<Button-1>", h_exit)

update_timer()
root.mainloop()