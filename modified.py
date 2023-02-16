import random
import tkinter as tk
import styles as s

def __init__(self): #initializing game window and organizing tkinter widgets into grid
    tk.Frame.__init__(self)
    self.grid()
    self.master.title('HFP - 2048')

    #grid size and style
    self.main_grid = tk.Frame(
        self, bg = s.boxColor, bd=3, width=400, height=400)
    self.main_grid.grid(pady=(80,0)) #vertical padding
    self.interface() #function for cell frames
    self.initGame() #function for game to commence

    #tkinter key binding for controls
    self.master.bind("<Left>", self.left)
    self.master.bind("<Right>", self.right)
    self.master.bind("<Up>", self.up)
    self.master.bind("<Down", self.down)