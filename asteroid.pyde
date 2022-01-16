from helpers import *
from Spaceship import Spaceship
from Rock import Rock
from Bullet import Bullet

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

# Bullets objects
bullets = []


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
        textSize(30)
        text("Score: ", 45, 60)
        draw_spaceship()
        
        update_bullets()
        draw_bullets()
        
        # circle(500, 500, 100)
        for rock in rocks:
            rock.update_pos()
            if rock.is_active:
                # rock.is_collide_with((500, 500), 100)
                if is_collided(spaceship, rock):
                    rock.is_active = False
                    # TODO: update animation/sound
                    circle(spaceship.pos_x, spaceship.pos_y, 50)
                else:
                    image(rock_img, rock.pos_x, rock.pos_y)
            
                
def mousePressed():
    global game_background
    if game_background == 1:
        if (mouseX > 429 and mouseX < 581) and (mouseY > 499 and mouseY < 551):
            game_background = 2
                 
def keyPressed():
    global spaceship, bullets
    if keyCode == UP:
        if spaceship.speed > -SPEED_LIMIT:
            spaceship.increase_speed(-SPEED_DELTA)
    elif keyCode == DOWN:
        spaceship.increase_speed(SPEED_DELTA)
        if spaceship.speed > 0:
            spaceship.speed = 0
    elif keyCode == LEFT:
        spaceship.angle -= ANGLE_DELTA
    elif keyCode == RIGHT:
        spaceship.angle += ANGLE_DELTA
    elif keyCode == 32:  # SPACE BUTTON
        # TODO: update sound
        bullets.append(Bullet(spaceship.points[0], spaceship.points[1], spaceship.angle, -30))

def update_bullets():
    global bullets, rocks
    
    for bullet in bullets:
        bullet.update_move()
        # Check the collision with rocks
        # TODO: increase score / update sound
        for rock in rocks:
            if bullet.is_active == True and is_collided(bullet, rock):
                bullet.is_active = False
                rock.is_active = False

    new_bullets = []
    for bullet in bullets:
        if bullet.is_active == True:
            new_bullets.append(bullet)
    bullets = new_bullets

def draw_bullets():
    global bullets
    for bullet in bullets:
        circle(bullet.x, bullet.y, bullet.size)

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

    # circle(spaceship.pos_x, spaceship.pos_y, 15)
    # circle(spaceship.pos_x, spaceship.pos_y+20, 25)
    
    # image(rock_img, 100, 100)
    # r_x = 295
    # r_y = 225
    # circle(100+r_x, 100+r_y, 70)


    
