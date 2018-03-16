from graphics import *
from person import *
from armor import *
import random
SKINTONES = [color_rgb(91,0,0),color_rgb(253,228,200),color_rgb(229,194,152),color_rgb(208,146,110)]
class Knight(Person):

    def __init__(self):
        super().__init__(random.choice(SKINTONES),win,"Knight",(425,162.5))
        armor = Armor((self.pos[0],self.pos[1]))
