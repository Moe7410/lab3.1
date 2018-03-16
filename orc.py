from graphics import *
from person import *
from armor import *
import random
class Orc(Person):
    """draws an orc"""

    def __init__(self):
        super().__init__(color_rgb(175,184,69),win,"Orc")
        self.drawNecklace()
        self.drawKilt()
        self.paint_color = None
        armorChance = (0,1)
        armor = random.choice(armorChance)
        if armor == 1:
             armor = Armor((self.pos[0],self.pos[1]))
        

    def drawHead(self):
        name = Text(Point(self.pos[0] + 75,self.pos[1] - 25),self.text)
        name.draw(win)
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
