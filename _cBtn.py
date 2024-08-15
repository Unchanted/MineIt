from tkinter import *
from _coordObj import Coord

class MSButton:
    def __init__(self, btn, val, coord, checked=False, flagged=False):
        self.btn = btn
        self.value = val
        self.coord = coord
        self.check = checked
        self.flagged = flagged

    def show(self):
        self.btn.grid(row=self.coord.x, column=self.coord.y)

    def getCoord(self):
        return self.coord

    def getVal(self):
        return self.value

class MSButtonList:
    def __init__(self):
        self.lst = []

    def add(self, msbutton):
        self.lst.append(msbutton)

    def _find_by_coord(self, r, c):
        if isinstance(r, Coord):
            r, c = r.x, r.y
        return next((msbtn for msbtn in self.lst if msbtn.coord.x == r and msbtn.coord.y == c), None)

    def get(self, r, c=None):
        msbtn = self._find_by_coord(r, c)
        return str(msbtn.value) if msbtn else None

    def getBtn(self, r, c=None):
        msbtn = self._find_by_coord(r, c)
        return msbtn.btn if msbtn else None

    def getMSBtn(self, r, c=None):
        return self._find_by_coord(r, c)

    def setVal(self, newVal, r, c=None):
        msbtn = self._find_by_coord(r, c)
        if msbtn:
            msbtn.value = newVal

    def exists(self, r, c=None):
        return self._find_by_coord(r, c) is not None
