import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_HEIGHT = TILE_SIZE * ROWS
WINDOW_WIDTH = TILE_SIZE * COLS

class Tile:
        def __init__(self,x,y):
            self.x = x
            self.y = y

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
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initialize game
snake = Tile(5*TILE_SIZE,5*TILE_SIZE) #single tile, snake's head
food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)

def draw():
    global snake      #using snake var within this function uses the global snake
    
    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "lime green")
    
    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "red")

    window.after(100,draw) #every 100ms, call draw function (10fps)

draw()

window.mainloop()                   #keeps window on