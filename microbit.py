# Add your Python code here. E.g.
from microbit import *
import random

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
        self.isAlive = False
        display.scroll("u ded fam")
        display.clear()
             
class Car():
    def __init__(self):
        self.x = random.randint(0,4)
        self.y = 0
        self.brightness = 5
        self.isOnScreen = True
        display.set_pixel(self.x, self.y, self.brightness)
         
    def move_down(self):
        if self.y != 4:
            display.set_pixel(self.x, self.y, 0)
            display.set_pixel(self.x, self.y+1, self.brightness)
            self.y += 1;
        else:
            self.kill();
    def kill(self):
        if self.isOnScreen:
            display.set_pixel(self.x, self.y, 0)
            self.isOnScreen = False
            makeNewCar()

def makeNewCar():
    global car
    car = Car()
        
frog = Frog(2)
car = Car()
counter = 0

while True:
    if button_a.was_pressed():
        frog.strafe("left")
    if button_b.was_pressed():
        frog.strafe("right")
    if int(running_time()/1000) != counter:
        counter += 1
        car.move_down()
        #display.scroll(str(int(running_time()/1000)))