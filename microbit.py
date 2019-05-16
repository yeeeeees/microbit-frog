# Add your Python code here. E.g.
from microbit import *
import random

def try_set_pixel(x, y, b):
    if x in range(0, 5) and y in range(0, 5):
        display.set_pixel(x, y, b)

def makeNewCar():
    global car
    car = Car()

class Frog():
    def __init__(self, x):
        self.x = x
        self.y = 4
        self.brightness = 7
        self.isAlive = True
        display.set_pixel(self.x, self.y, self.brightness)
    def strafe(self, pos):
        display.set_pixel(self.x, self.y, 0)
        if self.x < 4 and pos == "right":
            self.x += 1
        if self.x > 0 and pos == "left":
            self.x -=1
        display.set_pixel(self.x, self.y, self.brightness)  
    def die(self):
        #global score
        self.isAlive = False
        display.scroll("u ded fam")
        display.scroll("score : " + str(score))
        display.clear()
        
class Car():
    def __init__(self):
        global cars
        self.x = random.randint(0,4)
        self.y = 0
        self.parts = [[self.x, self.y], [self.x, self.y-1]]
        self.brightness = 4
        self.isOnScreen = True
        display.set_pixel(self.x, self.y, self.brightness)
        cars.append(self)
    def move_down(self):
        if self.y != 6:
            self.y += 1;
            self.parts = [[self.x, self.y], [self.x, self.y-1]]
            try_set_pixel(self.x, self.y-2, 0)
            try_set_pixel(self.x, self.y, self.brightness)
        else:
            self.kill();
    def kill(self):
        if self.isOnScreen:
            global score
            try_set_pixel(self.x, self.y-1, 0)
            self.isOnScreen = False
            makeNewCar()
            score += 1
        
frog = Frog(2)
cars = []
car = Car()
counter_spawn = 0
counter_move = 0
score = 0

while frog.isAlive:
    if button_a.was_pressed():
        frog.strafe("left")
    if button_b.was_pressed():
        frog.strafe("right")
    if int(running_time()/600) == counter_move:
        counter_move += 1
        for i in cars:
            i.move_down()
    if int(running_time()/5000) == counter_spawn:
        counter_spawn += 1
        #display.scroll(len(cars))
        if len(cars) < 4:
            car = Car()
    for i in cars:
        for j in i.parts:
            if (frog.x, frog.y) == (j[0], j[1]):
                frog.die()
        #display.scroll(str(int(running_time()/1000)))