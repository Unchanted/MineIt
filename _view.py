
from tkinter import *
from _root import Root

class View(Root):
    
    def __init__(self, parent=None):
        if parent != None:
            self.root = parent
        else:
            super().__init__()
        self.root.title("Minesweeper")
        imgicon = PhotoImage(file='_logo.gif')
        self.root.tk.call('wm', 'iconphoto', self.root._w, imgicon)  
        self.screen = Frame(self.root)

    def start(self):
        self.screen.grid()
        self.root.mainloop()

    def clear(self):
        self.screen.grid_forget()
        self.screen.destroy()

    def close(self):
        self.screen.grid_forget()
        self.screen.destroy()
        super().close()
