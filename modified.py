# modified functions:
#            used tkinter for game window ui
#            changed style and game design through styles module
#            modified the dsa into a simpler version
#            changed the structure for traversing, accessing, and manipulating matrix/game cells
#            added score increment and display

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
                bg = s.emptyCellColor,
                width = 130,
                height = 130
            )
            cell_frame.grid(row=i, column=j, padx=5, pady=5)
            cell_number = tk.Label(self.main_grid, bg=s.emptyCellColor)
            cell_number.grid(row=i, column=j)
            cell_data = {"frame": cell_frame, "number": cell_number}
            row.append(cell_data)
        self.cells.append(row)

    # for score display
    score_frame = tk.Frame(self)
    score_frame.place(relx=0.5, y=38, anchor="center")
    tk.Label(
        score_frame,
        text="Score",
        font=s.scoreTitleFont).grid(
        row=0)
    self.score_label = tk.Label(score_frame, text="0", font=s.scoreNumberFont)
    self.score_label.grid(row=1)

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

# functions for matrix manipulation 

def stack(self): # to compress all non-zero numbers in the matrix to one side of the board to eliminate empty cell gaps in between
    new_matrix = [[0] * 4 for _ in range(4)]
    for i in range(4):
        fill_position = 0
        for j in range(4):
            if self.matrix[i][j] != 0:
                new_matrix[i][fill_position] = self.matrix[i][j]
                fill_position += 1
    self.matrix = new_matrix

# pushing and merging horizontally adjacent cells with the same value (eg. 4 & 4 / 2 & 2) to the left most part of the matrix 

def combine(self):
    for i in range(4):
        for j in range(3):
            if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                self.matrix[i][j] *= 2
                self.matrix[i][j + 1] = 0
                self.score += self.matrix[i][j]

# appending empty list then reversing the value after the for loop to reverse the order of rows

def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

# flipping the matrix over its diagonal for up and down movement of the cells

def transpose(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix


# add a random tile with 2 or 4 value whenever an empty cell occurs
def addNewTile(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4])

# matching the matrix through updating the interface
def interfaceUpdate(self):
    for i in range(4):
        for j in range(4):
            cell_value = self.matrix[i][j]
            if cell_value == 0:
                self.cells[i][j]["frame"].configure(bg=s.emptyCellColor)
                self.cells[i][j]["number"].configure(
                    bg=s.emptyCellColor, text="")
            else:
                self.cells[i][j]["frame"].configure(
                    bg=s.cellColors[cell_value])
                self.cells[i][j]["number"].configure(
                    bg=s.cellColors[cell_value],
                    fg=s.cellColors[cell_value],
                    font=s.numberFonts[cell_value],
                    text=str(cell_value))
    self.score_label.configure(text=self.score)
    self.update_idletasks()