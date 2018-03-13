from graphics import *
import random
win = GraphWin("rpg",1000,650)
class Person(object):
    def __init__(self,color,pos = (75,25),eye = "black"):
        self.color = color
        self.eye = eye
        self.pos = pos
        self.drawHead()
        self.drawBody()
        self.drawArms()
        self.drawLegs()
    def drawHead(self):
        rectangle = Rectangle(Point(self.pos[0],self.pos[1]),Point(self.pos[0] + 150,self.pos[1] + 125))
        rectangle.draw(win)
        rectangle.setFill(self.color)
        position1 = (self.pos[0] + 25,self.pos[1]+50)
        for i in range(2):
            eye = Circle(Point(position1[0],position1[1]),12.5)
            eye.draw(win)
            eye.setFill(self.eye)
            position1 = (position1[0] + 100,position1[1])

    def drawBody(self):
        rectangle = Rectangle(Point(self.pos[0],self.pos[1] +125),Point(self.pos[0] + 150,self.pos[1] + 250))
        rectangle.draw(win)
        rectangle.setFill(self.color)
    def drawArms(self):
        position1 = (self.pos[0],self.pos[1]+125)
        for i in range(2):
            arm = Rectangle(Point(position1[0],position1[1]),Point(position1[0] - 50, position1[1] + 175))
            arm.draw(win)
            arm.setFill(self.color)
            position1 = (position1[0] + 200, position1[1])
    def drawLegs(self):
        rectangle = Rectangle(Point(self.pos[0],self.pos[1]+250),Point(self.pos[0] + 150, self.pos[1] + 375))
        rectangle.draw(win)
        rectangle.setFill(self.color)
        line = Line(Point(self.pos[0] + 75,self.pos[1] + 375), Point(self.pos[0] + 75, self.pos[1] + 275))
        line.draw(win)
class Orc(Person):
    """draws an orc"""

    def __init__(self):
        super().__init__(color_rgb(175,184,69),(75,25))
        self.drawNecklace()
        self.drawKilt()
        self.paint_color = None

    def drawHead(self):
        rectangle = Rectangle(Point(self.pos[0], self.pos[1]), Point(self.pos[0] + 150, self.pos[1] + 125))
        rectangle.draw(win)
        rectangle.setFill(self.color)
        position1 = (self.pos[0] + 25, self.pos[1] + 50)
        position2 = (self.pos[0] + 12.5,self.pos[1]+50)
        self.paint_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        for i in range(2): # eye paint
            paint = Polygon(Point(position2[0],position2[1]), Point(position2[0] + 25,position2[1]), Point(position2[0] + 12.5,position2[1]+ 50))
            paint.draw(win)
            paint.setFill(color_rgb(self.paint_color[0],self.paint_color[1],self.paint_color[2]))
            position2 = (position2[0] + 100,position2[1])
        triangle = Polygon(Point(self.pos[0] + 25, self.pos[1]), Point(self.pos[0] + 75,self.pos[1] + 50), Point(self.pos[0] + 125,self.pos[1])) # head paint
        triangle.draw(win)
        triangle.setFill(color_rgb(self.paint_color[0],self.paint_color[1],self.paint_color[2]))
        for i in range(2): # draws the eyes
            eye = Circle(Point(position1[0], position1[1]), 12.5)
            eye.draw(win)
            eye.setFill(self.eye)
            position1 = (position1[0] + 100, position1[1])

    def drawNecklace(self):
        arc = Arc(Point(self.pos[0],self.pos[1] + 100),Point(self.pos[0] +150,self.pos[1] + 150),0,-180,"arc")
        arc.draw(win)
        position1 = [[self.pos[0] + 75,self.pos[1] + 150],[self.pos[0] + 37.5,self.pos[1] + 146],[self.pos[0] + 112.5, self.pos[1] + 146]]
        for i in range(3):
            diamond = Polygon(Point(position1[i][0],position1[i][1]),Point(position1[i][0] + 6.25,position1[i][1] + 12.5),Point(position1[i][0],position1[i][1] + 25),Point(position1[i][0] - 6.25,position1[i][1] + 12.5))
            diamond.draw(win)
            diamond.setFill(color_rgb(self.paint_color[0],self.paint_color[1],self.paint_color[2]))

    def drawKilt(self):
        position1 = (self.pos[0],self.pos[1] + 250)
        kilt = Polygon(Point(position1[0],position1[1]),Point(position1[0] + 150,position1[1]),Point(position1[0] + 150,position1[1] + 75),Point(position1[0] + 112.5,position1[1] + 37.5),Point(position1[0] + 75,position1[1] + 62.5),Point(position1[0] + 37.5,position1[1] + 37.5),Point(position1[0],position1[1] + 75))
        kilt.draw(win)
        kilt.setFill(color_rgb(127, 86, 3))
        
        

class Armor(object):

    def __init__(self,pos,color = "gray"):
        self.pos = pos
        self.color = color

    def drawHelmet(self):
        helmet = Polygon(Point(self.pos[0],self.pos[1]),Point(self.pos[0] + 150,self.pos[1]),Point(self.pos[0] + 150,self.pos[1] + 125),Point(self.pos[0] + 100,self.pos[1] + 125),Point(self.pos[0] + 100,self.pos[1] + 100),Point(self.pos[0] + 137.5,self.pos[1] + 100),Point(self.pos[0] + 137.5,self.pos[1] + 25),Point(self.pos[0] + 100,self.pos[1] + 25),Point(self.pos[0] + 100,self.pos[1] + 87.5),Point(self.pos[0] + 50,self.pos[1] + 87.5),Point(self.pos[0] + 50,self.pos[1] + 25),Point(self.pos[0] + 12.5,self.pos[1] + 25),Point(self.pos[0] + 12.5,self.pos[1] + 100),Point(self.pos[0] + 50,self.pos[1] + 100),Point(self.pos[0] + 50,self.pos[1] + 125),Point(self.pos[0],self.pos[1] + 125))
        helmet.draw(win)
        helmet.setFill(self.color)
##    def drawChest(self):
##    def drawPants(self):
##    def drawGloves(self):
orc = Orc()
#person = Person("white")
#armor = Armor((75,25))
#armor.drawHelmet()
win.getMouse()
win.close()
