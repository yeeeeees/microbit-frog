# <center> Froggo : The Journey <center>
<center> A mix of Tetris and Crossy Road made for Micro:Bit microchips <center>

## Motivation
We were bored and made a little project using MicroPython. <br>
This project was never supposed to be a big project, but community feedback would be appreciated.

## Tech / Frameworks Used
* [microbit module](https://microbit.org/guide/python)
* [Python 3.6.7](https://www.python.org/)

## Code Example / API Reference 
MicroBit chip can't read python code, but it can read hex code. This python code is translated into hex code using [ this ](https://www.python.microbit.org/) python to hex converter. <br>
That converter has already microbit module installed so it is our go-to. <br>
<br>
We use heavy OOP style of code for this project while not being oversimplified.

```python
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
```
We are facing a big problem where after 25 cars have passed, the chip runs out of RAM memory and the program raises `MemoryError`. <br>
Every single feature is implemented through classes or functions. <br>
Micropython doesn't support [async](https://docs.python.org/3/library/asyncio.html) module.

## Tests
There aren't any tests need at the moment, but manual tests are really important. <br>
For this project, everything above Python 3.6 will be absolutely fine. Take a look [here](https://microbit-micropython.readthedocs.io/en/latest/) about micropython and it's features and limitations.


##  Contributing [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/yeeeeees/microbit-frog/issues)
We use a mixture of pylint and flake8 for linting. To contribute, fork this repo, add yourself to contributors list, make changes and submit PR.
Feel free to open issues, we are glad to hear feedback.

## LICENSE
[MIT](https://choosealicense.com/licenses/mit/) © Saki
