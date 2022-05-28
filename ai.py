
from player import Player
import random
from time import sleep

class AI (Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        self.gesture_select = random.choice([0,1,2,3,4])
        sleep(.5)
        print (f"The computer chooses {self.gestures[self.gesture_select]}")
        print("")



    
    