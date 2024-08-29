import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25
TEXT_OFFSET = 50

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
windowid = None #variable for closing the draw loop on gameover

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
snake_body = [] #multiple snake tiles
velocityX = 0
velocityY = 0
game_over = False
score = 0

def reset():
     global snake, food, snake_body, velocityX, velocityY, game_over, score
     snake_body.clear()
     velocityX = 0
     velocityY = 0
     game_over = False
     score = 0
     canvas.delete("all")
     snake = Tile(5*TILE_SIZE,5*TILE_SIZE) #single tile, snake's head
     food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)

     draw()
     




def change_direction(e): #e = event
    #print(e)
    #print(e.keysym)
    global velocityX, velocityY, game_over
    

    if (game_over and e.keysym == "space"):
          reset()
         
    if (game_over):
          return
    
    
    if (e.keysym == "Up" and velocityY != 1):
         velocityX = 0
         velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
         velocityX = 0
         velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
         velocityX = -1
         velocityY = 0
    elif (e.keysym == "Right" and velocityX !=-1):
         velocityX = 1
         velocityY = 0        
    
def move():
     global snake, food, snake_body, game_over, velocityX, velocityY, score
     
     #game over = stop snake from moving
     if (game_over):
          return
     
     #if snake passes window boundary, then game over
     if (snake.x < 0 or snake.x >=WINDOW_WIDTH or snake.y < 0 or snake.y >=WINDOW_HEIGHT):
          game_over = True
          return
     
     #collision with body
          #checks every tile in array for collision
     for tile in snake_body:
          if (snake.x == tile.x and snake.y ==tile.y):
                    game_over = True   
                    return

     #collision with food 
          #adds food to snakebody and draws a new food on random tile
     if (snake.x == food.x and snake.y == food.y):
          snake_body.append(Tile(food.x, food.y))
          food.x = random.randint(0, COLS-1) * TILE_SIZE
          food.y = random.randint(0, ROWS-1) * TILE_SIZE
          score += 1

     #update snake body
          #counts backward from end of snakebody, moves it into place of previous segment tile
     for i in range(len(snake_body)-1, -1, -1):
          tile = snake_body[i]
          if (i == 0):
               tile.x = snake.x
               tile.y = snake.y
          else:
               prev_tile = snake_body[i-1]
               tile.x = prev_tile.x
               tile.y = prev_tile.y

     snake.x += velocityX * TILE_SIZE
     snake.y += velocityY * TILE_SIZE

        

def draw():
    global snake, food, snake_body, game_over, score, windowid
                         #using snake var within this function uses the global snake
    
    move()              #calls move function (moves every 1/10 second or 10 frames per second)
    
    canvas.delete("all") #updates the board
     
    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "red")
    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "lime green")
    
    
    for tile in snake_body:
          canvas.create_rectangle(tile.x, tile.y, tile.x+TILE_SIZE, tile.y + TILE_SIZE, fill = "lime green")
          
          
    if (game_over):
         canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - TEXT_OFFSET * 2, font = "Arial 20", text = f"Game Over", fill = "white")
         canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - TEXT_OFFSET / 2, font = "Arial 15", text = f"Score: {score}", fill = "white")
         canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + TEXT_OFFSET, font = "Arial 15", text = "Try Again? (press space)", fill = "white")       
         window.after_cancel(windowid)  
    else:
         windowid = window.after(100,draw) #every 100ms, call draw function (10fps)
         canvas.create_text(30, 20, font = "Arial 10", text = f"Score: {score}", fill = "white")
    
  #  if (game_over == False):
          
   # else:
         
draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()                   #keeps window on