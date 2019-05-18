from microbit import *
import random

class Game():
    def __init__(self):
        self.frog = Frog(self, 2)
        self.cars = []
        car = Car(self)
        self.cars.append(car)
        self.counter_spawn = 0
        self.counter_move = 0
        self.score = 0
        self.isStarted = False
    def start(self):
        self.isStarted = True
        while self.isStarted:
            if button_a.was_pressed():
                self.frog.strafe("left")
            if button_b.was_pressed():
                self.frog.strafe("right")
            if int(running_time()/600) == self.counter_move:
                self.counter_move += 1
                for i in self.cars:
                    i.move_down()
            if int(running_time()/5000) == self.counter_spawn:
                self.counter_spawn += 1
                #display.scroll(len(cars))
                if len(self.cars) < 20:
                    car = Car(self)
                    self.cars.append(car)
            for i in self.cars:
                for j in i.parts:
                    if (self.frog.x, self.frog.y) == (j[0], j[1]):
                        self.frog.die()
                        self.isStarted = False
    @staticmethod
    def try_set_pixel(x, y, b):
        if x in range(0, 5) and y in range(0, 5):
            display.set_pixel(x, y, b)

class Frog():
    def __init__(self, game, x):
        self.game = game
        self.x = x
        self.y = 4
        self.brightness = 7
        self.isAlive = True
        self.game.try_set_pixel(self.x, self.y, self.brightness)
    def strafe(self, pos):
        self.game.try_set_pixel(self.x, self.y, 0)
        if self.x < 4 and pos == "right":
            self.x += 1
        if self.x > 0 and pos == "left":
            self.x -=1
        self.game.try_set_pixel(self.x, self.y, self.brightness)  
    def die(self):
        self.isAlive = False
        display.scroll("u ded fam")
        display.scroll("score: " + str(self.game.score))
        display.clear()
        
class Car():
    def __init__(self, game):
        self.game = game
        self.x = random.randint(0,4)
        self.y = 0
        self.parts = [[self.x, self.y], [self.x, self.y-1]]
        self.brightness = 4
        self.isOnScreen = True
        self.game.try_set_pixel(self.x, self.y, self.brightness)
    def move_down(self):
        if self.y != 6:
            self.update(self.y+1)
        else:
            self.reset()
    def update(self, y):
        self.y = y
        self.parts = [[self.x, self.y], [self.x, self.y-1]]
        self.game.try_set_pixel(self.x, self.y-2, 0)
        self.game.try_set_pixel(self.x, self.y, self.brightness)
    def reset(self):
        if self.isOnScreen:
            self.game.try_set_pixel(self.x, self.y-1, 0)
            self.isOnScreen = False
            self.game.score += 1
            self.update(self.y+1)

game = Game()
game.start()
