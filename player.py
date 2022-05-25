


gestures = ["rock", "paper", "scissors", "lizard", "Spock"]


class Player:
    def __init__(self):
        self.name = input("Type in your name:")
        self.gestures = input("Select a gesture:")
        self.score = 0

        
    def select_gesture(self):
        self.gestures = input(f"{self.name}, choose a gesture: rock, paper, scissor, lizard or spock.")
        if self.gestures == "rock":
            print("You have chosen: rock.")



        

    


        