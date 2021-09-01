import pygame as pg
from vector import Vector as V
from random import uniform


class Boid():

    def __init__(self, screen, position, velocity):
        self.screen = screen
        self.position = position
        self.velocity = velocity
        self.acceleration = V(0,0,0)

        self.max_Force = 20
        self.max_Speed = 10

        self.aPerception = 150.0
        self.cPerception = 100.0
        self.sPerception = 150.0

        self.aFactor = 1.5
        self.cFactor = 1.0
        self.sFactor = 1.5

          
    def changePerception(self,aPer,cPer,sPer):
        self.aPerception = aPer
        self.cPerception = cPer
        self.sPerception = sPer
              
    def changeFactor(self,aFac,cFac,sFac):
        self.aFactor = aFac
        self.cFactor = cFac
        self.sFactor = sFac

    def separation(self, boids):
        count = 0
        steer = V(0,0,0)

        for boid in boids:
            dist = self.position.dist(boid.position)
            if(dist > 0.0 and dist < self.cPerception):
                diff = self.position.sub(boid.position)
                diff.normalize()
                diff.div(dist)
                steer + diff
                count += 1
        
        if(count > 0):
            if(steer.getMagnitude()>0.0):
                steer.normalize()
                steer*self.max_Speed
                steer.sub(self.velocity) #Steer =  desired - velocity
                steer.limit(self.max_Force)

        count = 0
        return steer
        

    def alignment(self, boids):
        count = 0

        steer = V(0,0,0)

        for boid in boids:
            dist = self.position.dist(boid.position)
            if(dist > 0.0 and dist < self.aPerception):
                steer + boid.velocity
                count += 1
        
        if(count > 0):
            steer.div(count)
            steer-self.velocity
            steer.limit(self.max_Speed)

        count = 0
        return steer

    def cohesion(self, boids):
        count = 0
        steer = V(0,0,0)

        for boid in boids:
            dist = self.position.dist(boid.position)
            if(dist > 0.0 and dist < self.cPerception):
                steer + boid.position
                count += 1
        
        if(count > 0):
            steer.div(count)
            steer-self.position
            steer.setMagnitude(self.max_Speed)
            steer-self.velocity
            steer.limit(self.max_Force)

        count = 0
        return steer

    def flock(self,boids):
        a = self.alignment(boids)
        c = self.cohesion(boids)
        s = self.separation(boids)

        a*self.aFactor
        c*self.cFactor
        s*self.sFactor

        self.acceleration + a
        self.acceleration + c
        self.acceleration + s


    def borders(self):
        if(self.position.x > 999): self.position.x = 0
        if(self.position.x < 0): self.position.x = 999
        if(self.position.y > 999): self.position.y = 0
        if(self.position.y < 0): self.position.y = 999

    def update(self):
        self.velocity + self.acceleration
        self.velocity.limit(self.max_Speed)
        self.position + self.velocity

    def get_neighbors(self, boids):
        pass

    def render(self):
        pg.draw.circle(self.screen, (255,255,255), (self.position.x,self.position.y), (4))

        