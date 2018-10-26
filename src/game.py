#!/usr/local/bin/python3

import tkinter as tk
import random

SIGNS = ['<', '>', '=']

def new_game():
	l1.config(text=str(random.randint(0,9)))
	l3.config(text=str(random.randint(0,9)))

def exit_game():
	root.destroy()


root = tk.Tk()
root.title("HAI MATEI...")
root.geometry("500x500")
root.resizable(0, 0)

frame_top = tk.Frame(root, bg="yellow", height=300, width=500)
frame_top.grid(row=0, column=0)
frame_top.grid_propagate(0)
frame_bottom = tk.Frame(root, bg="red", height=200, width=500)
frame_bottom.grid(row=1, column=0)

# root.grid_rowconfigure(1, weight=1)
# root.grid_columnconfigure(0, weight=1)


frame_a = tk.Frame(frame_top, bg="green", height=100, width=100)
frame_a.grid(row=0, column=0)
frame_a.grid_propagate(0)
frame_b = tk.Frame(frame_top, bg="blue", height=100, width=100)
frame_b.grid(row=0, column=1)
frame_c = tk.Frame(frame_top, bg="grey", height=100, width=100)
frame_c.grid(row=0, column=2)

l1 = tk.Label(frame_a, text="A")
l1.grid(row=0, column=0)
# l2 = tk.Label(frame_top, padx=40, pady=100, bg="yellow", text="?")
# l2.grid(row=0, column=1)
# l3 = tk.Label(frame_top, padx=40, pady=100, text="C")
# l3.grid(row=0, column=2)

# btn_new_game = tk.Button(frame_bottom, text="New Game", width=10, command=new_game)
# btn_new_game.grid(row=0, column=0)
# btn_exit = tk.Button(frame_bottom, text="Exit", width=10, command=exit_game)
# btn_exit.grid(row=0, column=1)

root.mainloop()