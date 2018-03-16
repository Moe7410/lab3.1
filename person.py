from graphics import *
win = GraphWin("rpg",1000,650)
class Person(object):
    def __init__(self,color,win,text = "",pos = (425,162.5),eye = "black"):
        self.win = win
        self.rectangles = []
        self.color = color
        self.text = text
        self.eye = eye
        self.pos = pos
        self.drawHead()
        self.drawBody()
        self.drawArms()
        self.drawLegs()
    def drawHead(self):
        name = Text(Point(self.pos[0] + 75,self.pos[1] - 25),self.text)
        name.draw(self.win)
        rectangle = Rectangle(Point(self.pos[0],self.pos[1]),Point(self.pos[0] + 150,self.pos[1] + 125))
        rectangle.draw(self.win)
        rectangle.setFill(self.color)
        self.rectangles.append(rectangle)
        position1 = (self.pos[0] + 25,self.pos[1]+50)
        for i in range(2):
            eye = Circle(Point(position1[0],position1[1]),12.5)
            eye.draw(self.win)
            eye.setFill(self.eye)
            position1 = (position1[0] + 100,position1[1])

    def drawBody(self):
        rectangle = Rectangle(Point(self.pos[0],self.pos[1] +125),Point(self.pos[0] + 150,self.pos[1] + 250))
        rectangle.draw(self.win)
        rectangle.setFill(self.color)
        self.rectangles.append(rectangle)
    def drawArms(self):
        position1 = (self.pos[0],self.pos[1]+125)
        for i in range(2):
            arm = Rectangle(Point(position1[0],position1[1]),Point(position1[0] - 50, position1[1] + 175))
            arm.draw(self.win)
            arm.setFill(self.color)
            self.rectangles.append(arm)
            position1 = (position1[0] + 200, position1[1])
    def drawLegs(self):
        rectangle = Rectangle(Point(self.pos[0],self.pos[1]+250),Point(self.pos[0] + 150, self.pos[1] + 375))
        rectangle.draw(self.win)
        rectangle.setFill(self.color)
        self.rectangles.append(rectangle)
        line = Line(Point(self.pos[0] + 75,self.pos[1] + 375), Point(self.pos[0] + 75, self.pos[1] + 275))
        line.draw(self.win)
    
        


