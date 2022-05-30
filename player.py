from time import sleep
class Player:
    def __init__(self):
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.gesture = ""
        self.score = 0
        
    def select_gesture(self):
        while True:
            self.gesture_select = int(input("Choose a gesture. Enter 0 for rock, 1 for paper, 2 for scissor, 3 lizard or 4 for spock. "))
            print("")
            if self.gesture == 0:
                sleep(.5)
                print(f"You have chosen {self.gestures[0]}.")
                print("") 
            elif self.gesture == 1:
                sleep(.5)
                print(f"You have chosen {self.gestures[1]}.")
                print("") 
            elif self.gesture_select == 2: 
                sleep(.5)
                print(f"You have chosen {self.gestures[2]}.")
                print("") 
            elif self.gesture_select == 3:  
                sleep(.5) 
                print(f"You have chosen {self.gestures[3]}.")
                print("") 
            elif self.gesture_select == 3:  
                sleep(.5)    
                print(f"You have chosen {self.gestures[4]}.")
                print("") 
            if self.gesture_select not in [0, 1, 2, 3, 4]:
                sleep(.5)
                print("How about no? Numbers 0-4 only please.")
                print("") 
            else:
                break