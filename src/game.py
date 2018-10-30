#!/usr/local/bin/python3

import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk

a = -1
b = -1
right = 0
wrong = 0
status = "HAI..."
maxim = 100
no_questions = 30
photo_path = "photo/"

def init():
    global right
    global wrong
    right = 0
    wrong = 0
    status = "HAI..."
    label_top_a1.place(relx=0.5, rely=0.5)
    label_top_b1.place(relx=0.5, rely=0.5)
    label_top_c1.place(relx=0.5, rely=0.5)
    btn_big.place(relx=0.5, rely=0.5)
    btn_eq.place(relx=0.5, rely=0.5)
    btn_small.place(relx=0.5, rely=0.5)
    label_top_b3.place(relx=0.5, rely=0.5)
    label_top_a3.config(text=status)
    label_top_a3.place(relx=0.5, rely=0.5)
    btn_big.config(state=NORMAL)
    btn_eq.config(state=NORMAL)
    btn_small.config(state=NORMAL)
    new_game()

def h_new_game(event):
    init()

def h_exit(event):
    exit_game()


def new_game():
    global a
    global b
    global right
    global wrong
    global status
    global maxim
    global no_questions
    if right == no_questions:
        status = "BRAVO MATEI !!!"
        label_top_a3.config(text=status)
        btn_big.config(state=DISABLED)
        btn_eq.config(state=DISABLED)
        btn_small.config(state=DISABLED)
    elif wrong == no_questions:
        status = "GAME OVER!!!"
        label_top_a3.config(text=status)
        btn_big.config(state=DISABLED)
        btn_eq.config(state=DISABLED)
        btn_small.config(state=DISABLED)
    else: 
        a = random.randint(0, maxim)
        b = random.randint(0, maxim)
        label_top_a1.config(text=str(a))
        label_top_c1.config(text=str(b))
    label_top_b3.config(text=str(right) + " / " + str(wrong))

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


root = tk.Tk()
root.title("HAI MATEI...")
root.geometry("500x500")
root.resizable(0, 0)

frame_top = tk.Frame(root, bg="yellow", height=300, width=500)
frame_top.grid(row=0, column=0)
frame_top.grid_propagate(0)
frame_bottom = tk.Frame(root, bg="red", height=200, width=500)
frame_bottom.grid(row=1, column=0)
frame_bottom.grid_propagate(0)

frame_top_a1 = tk.Frame(frame_top, bg="green", height=100, width=100)
frame_top_a1.grid(row=0, column=0)
frame_top_a1.grid_propagate(0)
frame_top_b1 = tk.Frame(frame_top, bg="blue", height=100, width=100)
frame_top_b1.grid(row=0, column=1)
frame_top_c1 = tk.Frame(frame_top, bg="grey", height=100, width=100)
frame_top_c1.grid(row=0, column=2)
frame_top_a2 = tk.Frame(frame_top, bg="grey", height=100, width=100)
frame_top_a2.grid(row=1, column=0)
frame_top_b2 = tk.Frame(frame_top, bg="black", height=100, width=100)
frame_top_b2.grid(row=1, column=1)
frame_top_c2 = tk.Frame(frame_top, bg="brown", height=100, width=100)
frame_top_c2.grid(row=1, column=2)
frame_top_a3 = tk.Frame(frame_top, bg="red", height=100, width=300)
frame_top_a3.grid(row=2, column=0, columnspan=3)
frame_top_b3 = tk.Frame(frame_top, bg="grey", height=100, width=100)
frame_top_b3.grid(row=2, column=4)

label_top_a1 = tk.Label(frame_top_a1, text="A")
label_top_b1 = tk.Label(frame_top_b1, text="?")
label_top_c1 = tk.Label(frame_top_c1, text="B")
btn_big = tk.Button(frame_top_a2, text=">", command=is_big)
btn_eq = tk.Button(frame_top_b2, text="=", command=is_eq)
btn_small = tk.Button(frame_top_c2, text="<", command=is_small)
label_top_a3 = tk.Label(frame_top_a3, text="...STATUS...")
label_top_b3 = tk.Label(frame_top_b3, text="...")

frame_bottom_a1 = tk.Frame(frame_bottom, bg="green", height=100, width=150)
frame_bottom_a1.grid(row=0, column=0)
frame_bottom_a1.grid_propagate(0)
frame_bottom_b1 = tk.Frame(frame_bottom, bg="blue", height=100, width=150)
frame_bottom_b1.grid(row=0, column=1)

# btn_new_game = tk.Button(frame_bottom_a1, text="New Game", command=init)
# btn_new_game.place(relx=0, rely=0)
btn_exit = tk.Button(frame_bottom_b1, text="Exit", command=exit_game)
btn_exit.place(relx=0, rely=0)

img_new_game = ImageTk.PhotoImage(Image.open(photo_path + "new_game.jpg"))
label_new_game = tk.Label(frame_bottom_a1, image=img_new_game)
label_new_game.place(relx=0, rely=0, relwidth=1, relheight=1)
label_new_game.bind("<Button-1>", h_new_game)

img_exit = ImageTk.PhotoImage(Image.open(photo_path + "exit.jpg"))
label_exit = tk.Label(frame_bottom_b1, image=img_exit)
label_exit.place(relx=0, rely=0, relwidth=1, relheight=1)
label_exit.bind("<Button-1>", h_exit)


root.mainloop()