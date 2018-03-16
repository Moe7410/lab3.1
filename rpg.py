from graphics import *
from person import *
from orc import *
from knight import *
import random
import time
CHARACTERS = ["knight","orc"]
ORCPHOTOS = ["orccamp1.png","Orc_Camp-Main.png"]
KNIGHTPHOTOS = ["castle1.png","castle2.png"]
def main():
    while True:
        character = random.choice(CHARACTERS)
        if character == "knight":
            image =  Image(Point(500,325),random.choice(KNIGHTPHOTOS))
            image.draw(win)
            knight = Knight()
            
        else:
            image =  Image(Point(500,325),random.choice(ORCPHOTOS))
            image.draw(win)
            orc = Orc()
        time.sleep(15)
main()
win.getMouse()
win.close()
