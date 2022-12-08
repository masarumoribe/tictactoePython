import random
import time
from tkinter import messagebox
import tkinter as tk

class Cell:
    cells = []
    my_turn=True
    game_over = False
    def __init__(self, x, y, value=None):
        self.x = x
        self.y = y
        self.value = value
        self.btn_object = None
        Cell.cells.append(self)

    def create_btn_object(self, master):
        btn = tk.Button(master, width=11, height=6, font='Helvetica 25 bold')
        btn.bind('<Button-1>', self.clicked)
        self.btn_object = btn

    def clicked(self, event):
        if self.value == None and Cell.my_turn == True:
            self.btn_object.configure(text="X")
            self.value = "X"
            Cell.my_turn = False
            print(self.value)
            print(self.btn_object['text'])
            Cell.is_winner()
            if Cell.game_over == False:
                self.btn_object.after(1000, self.pc_turn)
        # print(Cell.cells)

    @classmethod
    def is_winner(cls, *args):
        if cls.cells[0].value == cls.cells[1].value == cls.cells[2].value == "X":
            messagebox.showinfo(message="You won Bitch!!!")
            cls.my_turn = True
            cls.game_over = True
        elif cls.cells[3].value == cls.cells[4].value == cls.cells[5].value == "X":
            messagebox.showinfo(message="You won Bitch!!!")
            cls.my_turn = True
            cls.game_over = True
        elif cls.cells[6].value == cls.cells[7].value == cls.cells[8].value == "X":
            messagebox.showinfo(message="You won Bitch!!!")
            cls.my_turn = True
            cls.game_over = True
        elif cls.cells[0].value == cls.cells[3].value == cls.cells[6].value == "X":
            messagebox.showinfo(message="You won Bitch!!!")
            cls.my_turn = True
            cls.game_over = True
        elif cls.cells[1].value == cls.cells[4].value == cls.cells[7].value == "X":
            messagebox.showinfo(message="You won Bitch!!!")
            cls.my_turn = True
            cls.game_over = True
        elif cls.cells[2].value == cls.cells[5].value == cls.cells[8].value == "X":
            messagebox.showinfo(message="You won Bitch!!!")
            cls.my_turn = True
            cls.game_over = True
        elif cls.cells[0].value == cls.cells[4].value == cls.cells[8].value == "X":
            messagebox.showinfo(message="You won Bitch!!!")
            cls.my_turn = True
            cls.game_over = True
        elif cls.cells[2].value == cls.cells[4].value == cls.cells[6].value == "X":
            messagebox.showinfo(message="You won Bitch!!!")
            cls.my_turn = True
            cls.game_over = True
        elif cls.cells[0].value == cls.cells[1].value == cls.cells[2].value == "O":
            messagebox.showinfo(message="You lost Bitchycita :(")
            cls.game_over = True
        elif cls.cells[3].value == cls.cells[4].value == cls.cells[5].value == "O":
            messagebox.showinfo(message="You lost Bitchycita :(")
            cls.game_over = True
        elif cls.cells[6].value == cls.cells[7].value == cls.cells[8].value == "O":
            messagebox.showinfo(message="You lost Bitchycita :(")
            cls.game_over = True
        elif cls.cells[0].value == cls.cells[3].value == cls.cells[6].value == "O":
            messagebox.showinfo(message="You lost Bitchycita :(")
            cls.game_over = True
        elif cls.cells[1].value == cls.cells[4].value == cls.cells[7].value == "O":
            messagebox.showinfo(message="You lost Bitchycita :(")
            cls.game_over = True
        elif cls.cells[2].value == cls.cells[5].value == cls.cells[8].value == "O":
            messagebox.showinfo(message="You lost Bitchycita :(")
            cls.game_over = True
        elif cls.cells[0].value == cls.cells[4].value == cls.cells[8].value == "O":
            messagebox.showinfo(message="You lost Bitchycita :(")
            cls.game_over = True
        elif cls.cells[2].value == cls.cells[4].value == cls.cells[6].value == "O":
            messagebox.showinfo(message="You lost Bitchycita :(")
            cls.game_over = True
        
    @classmethod
    def pc_turn(*args):
        while True:
            pc_choice = random.choice(Cell.cells)
            if pc_choice.value == None:
                pc_choice.btn_object.configure(text="O")
                pc_choice.value = "O"
                Cell.is_winner()
                Cell.my_turn = True
                break

    def __repr__(self):
        return f"Cell({self.x},{self.y},{self.value})"