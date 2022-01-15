import random
from helpers import init_asteroids
from Spaceship import Spaceship
from Rock import Rock

NUM_ROCKS_MAIN = 15
MODE_GAME_START = 1
MODE_GAME_ON = 2

game_background = MODE_GAME_START


spaceship = Spaceship()

# Rock objects
rock_img = None
rocks = []
for i in range(NUM_ROCKS_MAIN):
    rock = Rock()
    rocks.append(rock)



def setup():
    global rocks, rock_img
    size(1000, 800)
    rock_img = loadImage("Asteroid.png")
   
def draw():
    global rocks, rock_img
    if game_background == MODE_GAME_START:
        background(0)
        for rock in rocks:
            rock.update_pos()
            image(rock_img, rock.pos_x, rock.pos_y)


        textSize(80)
        text("Asteroids",330,200)
        fill(255,255,255)
        textSize(20)
        text("ARCADE GAME", 430,250)
        fill(255,255,255)
        rect(430,500,150,50)
        fill(0)
        textSize(20)
        text("Play Game",455,530)
        fill(255,255,255)
        
    elif game_background == MODE_GAME_ON:
        background(0)
        draw_spaceship()
        textSize(30)
        text("Score: ", 45, 60)
        for rock in rocks:
            rock.update_pos()
            image(rock_img, rock.pos_x, rock.pos_y)
                
def mousePressed():
    global game_background
    if game_background == 1:
        if (mouseX > 429 and mouseX < 581) and (mouseY > 499 and mouseY < 551):
            game_background = 2
                 
def keyPressed():
    global spaceship
    if keyCode == UP:
        spaceship.increase_speed(-0.5)
    elif keyCode == DOWN:
        spaceship.increase_speed(0.5)
    elif keyCode == RIGHT:
        spaceship.angle += 1
        # pushMatrix()
        # translate(width/2,height/2)
        # rotate(radians(90))
        # triangle(spaceshipx, spaceshipy, 375, 680, 425, 680)
        # popMatrix()
    
def draw_spaceship():
    global spaceship
    strokeWeight(2)
    stroke(255,140,0)
    noFill()
    triangle(*spaceship.get_draw_coord())


    
