from cell import Cell
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
# root.configure(bg='black')
root.geometry('600x620')
root.title('Tic-Tac-Toe Bitch!')
root.resizable(False, False)

top_frame = tk.Frame(root, bg='black', width=600, height=60)
top_frame.pack()

bottom_frame = tk.Frame(root, width=600, height=530)
bottom_frame.pack()

for i in range(3):
    for j in range(3):
        c = Cell(i, j)
        c.create_btn_object(bottom_frame)
        c.btn_object.grid(column=j, row=i)  

root.mainloop()

