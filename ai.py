
from player import Player
import random

class AI (Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        self.ai_gesture_select = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
        print (f"The computer chooses {self.ai_gesture_select%[0]}")



    
    