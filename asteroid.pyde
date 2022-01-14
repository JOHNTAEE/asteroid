import random
from helpers import init_asteroids
from Spaceship import Spaceship

spaceship = Spaceship()

# comment update more
x = 0
y = 0
asteroid = []
asteroidy = []
asteroidx = []
xspeed = []
yspeed = []


asteroidx, asteroidy, xspeed, yspeed = init_asteroids()

game_background = 1


def setup():
    global asteroid 
    size(1000, 800)
    for i in range(15):
        asteroid.append(loadImage("Asteroid.png"))
   
def draw():
    global x,y,asteroidy,asteroidx,asteroid,xspeed,yspeed,spaceshipx,spaceshipy
    if game_background == 1:
        background(0)
        if len(xspeed) > 0 and len(yspeed) > 0:
            for i in range(15):
                x+=xspeed[i]
                y+=yspeed[i]
                asteroidx[i] += xspeed[i]
                asteroidy[i] += yspeed[i]
                image(asteroid[i],asteroidx[i],asteroidy[i])
                
                if asteroidx[i] >= 1200:
                    asteroidx[i] = -400
                if asteroidy[i] >= 1000:
                    asteroidy[i] = -400
                if asteroidx[i] <= -500:
                    asteroidx[i] = 1000
                if asteroidy[i] <= -500:
                    asteroidy[i] = 800

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
        
    elif game_background == 2:
        background(0)
        draw_spaceship()
        textSize(30)
        text("Score: ", 45, 60)
        if len(xspeed) > 0 and len(yspeed) > 0:
            for i in range(5):
                x+=xspeed[i]
                y+=yspeed[i]
                asteroidx[i] += xspeed[i]
                asteroidy[i] += yspeed[i]
                image(asteroid[i],asteroidx[i],asteroidy[i])
                
                if asteroidx[i] >= 1200:
                    asteroidx[i] = -400
                if asteroidy[i] >= 1000:
                    asteroidy[i] = -400
                if asteroidx[i] <= -500:
                    asteroidx[i] = 1000
                if asteroidy[i] <= -500:
                    asteroidy[i] = 800
                
def mousePressed():
    global game_background
    if game_background == 1:
        if (mouseX > 429 and mouseX < 581) and (mouseY > 499 and mouseY < 551):
            game_background = 2
                 
def keyPressed():
    global spaceship
    if keyCode == UP:
        print 'up'
        spaceship.pos_y -= 10
        spaceship.speed_y += 2
    elif keyCode == DOWN:
        spaceship.pos_y += 10
        spaceship.speed_y -= 2
    elif keyCode == RIGHT:
        pass
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


    
