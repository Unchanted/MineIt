
from tkinter import *
from tkinter import ttk
from _view import View
import _menu

class Difficulty(View):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScreen()
        self.start()

    # Set difficulty value
    def select(self):
        self.newDiff = self.v.get()

    # Save difficulty and exit
    def saveAndExit(self):
        with open('_settings.txt', 'w+') as file:
            file.write(f"Difficulty:\t{self.newDiff}")
        self.clear()
        _menu.Menu(self.root)

    # Initialize difficulty selection screen
    def setScreen(self):
        self.newDiff = 0
        with open('_settings.txt', 'r') as inputFile:
            for line in inputFile:
                if "Difficulty:" in line:
                    self.newDiff = int(line.split('\t')[1])

        self.v = IntVar(self.screen, self.newDiff)
        Label(self.screen, text="Choose Difficulty:").grid(row=1, column=1)
        self.easy = Radiobutton(self.screen, text="Easy", variable=self.v, value=0, command=self.select)
        self.normal = Radiobutton(self.screen, text="Normal", variable=self.v, value=1, command=self.select)
        self.hard = Radiobutton(self.screen, text="Hard", variable=self.v, value=2, command=self.select)
        
        self.easy.grid(sticky="W", row=3, column=1)
        self.normal.grid(sticky="W", row=4, column=1)
        self.hard.grid(sticky="W", row=5, column=1)
        ttk.Button(self.screen, text="OK", command=self.saveAndExit).grid(row=7, column=1)
        
        for i in range(9):
            self.screen.grid_rowconfigure(i, minsize=20)
        for i in range(3):
            self.screen.grid_columnconfigure(i, minsize=20)
