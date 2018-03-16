from graphics import *
from person import win
import random
class Armor(object):

    def __init__(self,pos):
        self.pos = pos
        self.color = color_rgb(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        self.drawHelmet()
        self.drawChestPlate()
        self.drawGloves()
        self.drawPants()
    def drawHelmet(self):
        helmet = Polygon(Point(self.pos[0],self.pos[1]),Point(self.pos[0] + 150,self.pos[1]),Point(self.pos[0] + 150,self.pos[1] + 125),Point(self.pos[0] + 100,self.pos[1] + 125),Point(self.pos[0] + 100,self.pos[1] + 100),Point(self.pos[0] + 137.5,self.pos[1] + 100),Point(self.pos[0] + 137.5,self.pos[1] + 25),Point(self.pos[0] + 100,self.pos[1] + 25),Point(self.pos[0] + 100,self.pos[1] + 87.5),Point(self.pos[0] + 50,self.pos[1] + 87.5),Point(self.pos[0] + 50,self.pos[1] + 25),Point(self.pos[0] + 12.5,self.pos[1] + 25),Point(self.pos[0] + 12.5,self.pos[1] + 100),Point(self.pos[0] + 50,self.pos[1] + 100),Point(self.pos[0] + 50,self.pos[1] + 125),Point(self.pos[0],self.pos[1] + 125))
        helmet.draw(win)
        helmet.setFill(self.color)
    def drawChestPlate(self):
        newPos = (self.pos[0], self.pos[1] + 125) # upper left corner of chestplate
        rectangle = Rectangle(Point(newPos[0],newPos[1]),Point(newPos[0] + 150,newPos[1] + 125))
        rectangle.draw(win)
        rectangle.setFill(self.color)
        line = Line(Point(newPos[0] + 75,newPos[1]),Point(newPos[0] + 75, newPos[1] + 125))
        line.draw(win)
        arc = Arc(Point(newPos[0] - 37.5, newPos[1] - 37.5),Point(newPos[0] + 37.5, newPos[1] + 37.5),0,-90,"sector")
        arc.draw(win)
        arc = Arc(Point(arc.p1.getX() + 150, arc.p1.getY()),Point(arc.p2.getX() + 150, arc.p2.getY()),180, 90)
        arc.draw(win)
    def drawPants(self):
        newPos = (self.pos[0],self.pos[1] + 250)
        pants = Rectangle(Point(newPos[0],newPos[1]),Point(newPos[0] + 150, newPos[1] + 125))
        pants.draw(win)
        pants.setFill(self.color)
        line = Line(Point(newPos[0] + 75,newPos[1]),Point(newPos[0] + 75, newPos[1] + 125))
        line.draw(win)
    def drawGloves(self):
        newPos = (self.pos[0] - 50,self.pos[1] + 125) # upper left corner of shoulder pad
        for i in range(2):
            shoulderPad = Rectangle(Point(newPos[0],newPos[1]),Point(newPos[0] + 50, newPos[1] + 75))
            shoulderPad.draw(win)
            shoulderPad.setFill(self.color)
            glove = Rectangle(Point(newPos[0],newPos[1] + 125),Point(newPos[0] + 50, newPos[1] + 175))
            glove.draw(win)
            glove.setFill(self.color)
            newPos = (newPos[0] + 200, newPos[1])

