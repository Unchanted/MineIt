from tkinter import *

class Root():

    def __init__(self):
        self.root = Tk()

    def close(self):
        self.root.destroy()
        exit()
