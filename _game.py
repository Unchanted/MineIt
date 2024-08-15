from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from _view import View
from _coordObj import Coord
from _cBtn import *
import _menu
import random
import time

class Game(View):
    def __init__(self, parent=None):
        super().__init__(parent or None)
        self.timerS = time.time()
        self.mineCoordList = []
        self.btnList = MSButtonList()
        self.setScreen()
        self.start()

    def endGame(self):
        self.clear()
        _menu.Menu(self.root)

    def win(self):
        self.timerE = time.time()
        self.time = self.timerE - self.timerS
        player_name = simpledialog.askstring("Minesweeper",
                                             "Congratulations, you won!\nPlease enter your name:",
                                             parent=self.screen)
        if player_name:
            with open('_scores.txt', 'a+') as file:
                file.write(f"{player_name}\t{int(round(self.time))}\t{self.diff}\t\n")
        self.endGame()

    def checkWin(self):
        for i in range(self.height):
            for j in range(self.width):
                c = Coord(j, i)
                mb = self.btnList.getMSBtn(c)
                if not mb.check and c not in self.mineCoordList:
                    return
        self.win()

    def getImmediateCoordList(self, coord):
        imCoords = [Coord(coord.x-1, coord.y-1+i) for i in range(3)]
        imCoords += [Coord(coord.x+1, coord.y-1+i) for i in range(3)]
        imCoords += [Coord(coord.x, coord.y-1), Coord(coord.x, coord.y+1)]
        return imCoords

    def getImmediateMineCount(self, coord):
        surroundingMines = sum(
            1 for i in range(3)
            if self.btnList.get(coord.x-1, coord.y-1+i) == 'M' or
               self.btnList.get(coord.x+1, coord.y-1+i) == 'M'
        )
        if self.btnList.get(coord.x, coord.y-1) == 'M':
            surroundingMines += 1
        if self.btnList.get(coord.x, coord.y+1) == 'M':
            surroundingMines += 1
        return surroundingMines

    def btnClick(self, c):
        v = self.btnList.get(c)
        b = self.btnList.getBtn(c)
        mb = self.btnList.getMSBtn(c)

        if not mb.check:
            mb.check = True
            if v == 'M':
                b.config(bg="red")
                messagebox.showinfo("Minesweeper", "Y O U\tD I E D")
                with open('_dc.txt', 'r') as file:
                    dc = int(file.readline())
                with open('_dc.txt', 'w') as file:
                    file.write(str(dc + 1))
                self.endGame()
            elif v != 'NIL':
                b.config(bg="#aaaaaa", text=str(v))
            else:
                b.config(bg="#aaaaaa")
                for spot in self.getImmediateCoordList(c):
                    if self.btnList.exists(spot):
                        self.btnClick(spot)
        self.checkWin()
