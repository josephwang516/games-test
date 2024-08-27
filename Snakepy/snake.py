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
window.resizable(False, False)      #keeps height+width from changing


canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth =0, highlightthickness = 0 )
canvas.pack()
window.update()

#center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h) + (x) + (y)"
window.geometry(f"{window_width} x {window_height} + {window_x} + {window_y}")



window.mainloop()                   #keeps window on