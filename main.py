# Import non-standard modules.
import pygame as pg
from pygame.locals import *
from vector import Vector as v

#For creating random positions
import random as random
from datetime import datetime

from slider import Slider


# Import local modules
from boid import Boid

numOfBoids = 150
window_height = 800
window_width = 800
screenColor = (255,255,255)

listOfBoids = []
#Title and Icon load for window object
pg.display.set_caption("Boid simulation")
icon = pg.image.load('logo32x32.png')
pg.display.set_icon(icon)

#Creating the screen instance
#Note pos 0,0 is at the top left
screen = pg.display.set_mode((window_height,window_width))

def pointInRectanlge(px, py, rw, rh, rx, ry):
    if px > rx and px < rx  + rw:
        if py > ry and py < ry + rh:
            return True
    return False

def createBoids():
    for i in range(numOfBoids):
        tmp = Boid(screen,createRandomVector(0,window_height,i),createRandomVector(0,window_height,i))
        listOfBoids.append(tmp)

def createRandomVector(a,b,i):

    random.seed(datetime.now().second+i)

    x = random.randrange(a,b,2)
    y = random.randrange(a,b,2)
    z = random.randrange(a,b,2)
    res = v(x,y,z)
    return res

def main():
    # Create init object
    pg.init()


    mouse = pg.mouse
    #Slider(Position,highest value,width,text)
    sliderA = Slider((500, 0),200,20,"Alignment")
    sliderC = Slider((500, 100),200,30,"Cohesion")
    sliderS = Slider((500, 200),200,30,"Seperation")
    sliderAF = Slider((500, 300),10,30,"Alignment factor")
    sliderCF = Slider((500, 400),10,30,"Cohesion factor")
    sliderSF = Slider((500, 500),10,30,"Seperation factor")

    createBoids()
    #Loop here for screen
    running = True
    while running:

        #RGB values for screen
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        screen.fill((0,0,0))

        for boid in listOfBoids:
            boid.changePerception(sliderA.getValue(),sliderC.getValue(),sliderS.getValue())
            boid.changeFactor(sliderAF.getValue(),sliderCF.getValue(),sliderSF.getValue())
            boid.borders()
            boid.flock(listOfBoids)
            boid.update()
            boid.render()
        sliderAF.changeValue()
        sliderCF.changeValue()
        sliderSF.changeValue()
        sliderA.changeValue()
        sliderC.changeValue()
        sliderS.changeValue()
        sliderA.render(screen)
        sliderC.render(screen)
        sliderS.render(screen)
        sliderAF.render(screen)
        sliderCF.render(screen)
        sliderSF.render(screen)
        pg.display.update()

class Slider:
    def __init__(self, position:tuple, upperValue:int=10, sliderWidth:int = 30, text:str="Editing features for simulation",outlineSize:tuple=(300, 100))->None:
        self.position = position
        self.outlineSize = outlineSize
        self.text = text
        self.sliderWidth = sliderWidth
        self.upperValue = upperValue

    #returns the current value of the slider
    def getValue(self)->float:
        return self.sliderWidth / (self.outlineSize[0] / self.upperValue)

    #renders slider and the text showing the value of the slider
    def render(self, display:pg.display)->None:
        #draw outline and slider rectangles
        pg.draw.rect(display, (255, 0, 0), (self.position[0], self.position[1], 
                                              self.outlineSize[0], self.outlineSize[1]), 3)
        
        pg.draw.rect(display, (0, 255, 0), (self.position[0], self.position[1], 
                                              self.sliderWidth, self.outlineSize[1] - 10))

        #determite size of font
        self.font = pg.font.Font(pg.font.get_default_font(), int((15/100)*self.outlineSize[1]))

        #create text surface with value
        valueSurf = self.font.render(f"{self.text}: {round(self.getValue())}", True, (255, 0, 0))
        
        #centre text
        textx = self.position[0] + (self.outlineSize[0]/2) - (valueSurf.get_rect().width/2)
        texty = self.position[1] + (self.outlineSize[1]/2) - (valueSurf.get_rect().height/2)

        display.blit(valueSurf, (textx, texty))

    #allows users to change value of the slider by dragging it.
    def changeValue(self)->None:
        #If mouse is pressed and mouse is inside the slider
        mousePos = pg.mouse.get_pos()
        if pointInRectanlge(mousePos[0], mousePos[1]
                            , self.outlineSize[0], self.outlineSize[1], self.position[0], self.position[1]):
            if pg.mouse.get_pressed()[0]:
                #the size of the slider
                self.sliderWidth = mousePos[0] - self.position[0]

                #limit the size of the slider
                if self.sliderWidth < 1:
                    self.sliderWidth = 0
                if self.sliderWidth > self.outlineSize[0]:
                    self.sliderWidth = self.outlineSize[0]

main()