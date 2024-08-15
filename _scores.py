from tkinter import *
from tkinter import ttk
from _view import View
import _menu

class Scores(View):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScreen()
        self.start()

    # Exits and returns to main menu
    def returnCmd(self):
        self.clear()
        _menu.Menu(self.root)

    # Fetch and return top 10 scores for current difficulty
    def getInfo(self):
        difficulty = self._get_difficulty()

        with open('_scores.txt', 'r') as file:
            scores = {}
            for line in file:
                name, time, diff = line.split('\t')
                if int(diff) == difficulty:
                    time = int(time)
                    if name not in scores or time < scores[name]:
                        scores[name] = time
                        
            top_scores = sorted(scores.items(), key=lambda x: x[1])[:10]
            return top_scores

    # Get difficulty from settings
    def _get_difficulty(self):
        with open('_settings.txt', 'r') as file:
            for line in file:
                if "Difficulty:" in line:
                    return int(line.split('\t')[1])
        return 0  # Default difficulty if not found
