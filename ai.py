
from player import Player
import random

class AI (Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        self.gesture = random.choice([0,1,2,3,4])
        print (f"The computer chooses {self.gestures[self.gesture]}")



    
    