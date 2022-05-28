
class Player:
    def __init__(self):
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.gesture = ""
        self.score = 0
        
    def select_gesture(self):
        while True:
            self.gesture_select = int(input("Choose a gesture. Enter 0 for rock, 1 for paper, 2 for scissor, 3 lizard or 4 for spock."))
            if self.gesture == 0:
                print(f"You have chosen,{self.gestures[0]}")
            elif self.gesture == 1:
                print(f"You have chosen {self.gestures[1]}")
            elif self.gesture_select == 2: 
                print(f"You have chosen {self.gestures[2]}")
            elif self.gesture_select == 3:        
                print(f"You have chosen {self.gestures[3]}")
            elif self.gesture_select == 3:        
                print(f"You have chosen {self.gestures[4]}")
            if self.gesture_select not in [0, 1, 2, 3, 4]:
                print("Please try again. Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock: ")
            else:
                break