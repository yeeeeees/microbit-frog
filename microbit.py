# Add your Python code here. E.g.
from microbit import *
import random
import asyncio

class Frog():
    def __init__(self, x):
        self.x = x 
        self.y = 4
        self.isAlive = True
        display.set_pixel(self.x,self.y,9)
    
    def strafe(self, pos):
        display.set_pixel(self.x,self.y,0)
        if self.x < 4 and pos == "right":
            self.x += 1
        if self.x > 0 and pos == "left":
            self.x -=1
        display.set_pixel(self.x,self.y,9)
        
    
    def die(self):
        self.isAlive = False
        display.scroll("u ded fam")
        display.clear()
        
        
class Car():
    def __init__(self):
        self.x = random.randint(0,4)
        self.y = 0
        self.isOnScreen = True
        display.set_pixel(self.x,self.y,5)
        move_down()
         
    #investigate error hapenning here <-- async stuff
    async def move_down(self):
        while self.isOnScreen:
            if self.y ==4:
                break
            display.set_pixel(self.x,self.y,0)
            await display.set_pixel(self.x,self.y+1,5)
            asyncio.sleep(500)
        
        
        
        

frog = Frog(2)


while frog.isAlive:
    car = Car()
    if not frog.isAlive:
        quit()
    
    if button_a.was_pressed():
        frog.strafe("left")
        
    if button_b.was_pressed():
        frog.strafe("right")

    
    
    
    
    
    
    
    
    
    
    
    
        