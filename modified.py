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

    #running the tkinter event loop
    self.mainloop()

def interface(self):
    # making grids in array structure
    self.cells = []
    for i in range(4):
        row = []
        for j in range(4):
            cell_frame = tk.Frame(
                self.main_grid,
                bg = s.cellColor,
                width = 130,
                height = 130
            )
            cell_frame.grid(row=i, column=j, padx=5, pady=5)
            cell_number = tk.Label(self.main_grid, bg=s.cellColor)
            cell_number.grid(row=i, column=j)
            cell_data = {"frame": cell_frame, "number": cell_number}
            row.append(cell_data)
        self.cells.append(row)

def initGame(self):
    #matrix of 0
    self.matrix = [[0] * 4 for _ in range(4)]

    #filling grids with 2s in random positions
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    self.matrix[row][col] = 2
    self.cells[row][col]["frame"].configure(bg=s.cellColors[2])
    self.cells[row][col]["number"].configure(
    bg=s.cellColors[2],
    fg=s.cellNumberColors[2],
    font=s.numberFonts[2],
    text="2")
    while(self.matrix[row][col] != 0):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
    self.matrix[row][col] = 2
    self.cells[row][col]["frame"].configure(bg=s.cellColors[2])
    self.cells[row][col]["number"].configure(
        bg=s.cellColors[2],
        fg=s.cellNumberColors[2],
        font=s.numberFonts[2],
        text="2")