import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_HEIGHT = TILE_SIZE * ROWS
WINDOW_WIDTH = TILE_SIZE * COLS


#game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)  #keeps height+width from changing

window.mainloop()               #keeps window on