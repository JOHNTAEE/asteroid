from helpers import *
from Spaceship import Spaceship
from Rock import Rock

NUM_ROCKS_MAIN = 15
MODE_GAME_START = 1
MODE_GAME_ON = 2

ANGLE_DELTA = 5
SPEED_DELTA = 0.5
SPEED_LIMIT = 3

game_background = MODE_GAME_START

# Spaceship object
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
        # circle(500, 500, 100)
        for rock in rocks:
            rock.update_pos()
            if rock.is_active:
                # rock.is_collide_with((500, 500), 100)
                if is_collided(spaceship, rock):
                    rock.is_active = False
                    print("rock collision")
                    # TODO: update animation
                    circle(spaceship.pos_x, spaceship.pos_y, 50)
                else:
                    image(rock_img, rock.pos_x, rock.pos_y)
            
                
def mousePressed():
    global game_background
    if game_background == 1:
        if (mouseX > 429 and mouseX < 581) and (mouseY > 499 and mouseY < 551):
            game_background = 2
                 
def keyPressed():
    global spaceship
    if keyCode == UP:
        if spaceship.speed > -SPEED_LIMIT:
            spaceship.increase_speed(-SPEED_DELTA)
    elif keyCode == DOWN:
        spaceship.increase_speed(SPEED_DELTA)
        if spaceship.speed > SPEED_LIMIT/2:
            spaceship.speed = SPEED_LIMIT/2
    elif keyCode == LEFT:
        spaceship.angle -= ANGLE_DELTA
    elif keyCode == RIGHT:
        spaceship.angle += ANGLE_DELTA
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
    spaceship.get_draw_coord()
    triangle(*spaceship.points)
    
    # Debuggin outputs
    col_circles = spaceship.get_collision_circles()
    for col_circle in col_circles:
        circle(col_circle.x, col_circle.y, col_circle.diameter)

    if spaceship.is_out_of_screen():
        if spaceship.is_inside == True:
            print("out of screen")
            spaceship.pos_x = width - spaceship.pos_x
            spaceship.pos_y = height - spaceship.pos_y
            # spaceship.pos_x = 800 - spaceship.pos_x
            # spaceship.pos_y = 500 - spaceship.pos_y
            spaceship.is_inside = False
    else:
        spaceship.is_inside = True
    # circle(spaceship.pos_x, spaceship.pos_y, 15)
    # circle(spaceship.pos_x, spaceship.pos_y+20, 25)
    
    # image(rock_img, 100, 100)
    # r_x = 295
    # r_y = 225
    # circle(100+r_x, 100+r_y, 70)


    
