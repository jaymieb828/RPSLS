

from human import Human
from ai import AI
from time import sleep

player_1 = Human()
player_2 = AI()
    
class Game:
    def __init__(self) -> None:
        self.player_1 = Human()
        self.player_2 = None
        
    def welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock.")
        print("")
        sleep(.5)
        print("Each match will be best of three games.")
        print("")   
        sleep(.5)
        print("Use the number keys to enter your gesture choice.")
        print("")
        sleep(.5)

    def run_game(self):
        self.welcome()
        self.player_select()
        self.game_logic()
        self.score_keeping()
        

    def player_select(self):
        player_response = int(input("Enter 1 to play with another person. Enter 2 to play against the computer. "))
        if int(player_response) == 1:
            player_response = self.player_2 = Human()
            sleep(.5)
            print("") 
            print(f"You have chosen to play against another Player!")
            print("")
        elif int(player_response) == 2:
            player_response = self.player_2 = AI()
            sleep(.5)
            print("")
            print(f"You have chosen to play against the Computer!")
            print("")
        else:
            sleep(.5)
            print("")
            print("Please select either 1 or 2 to continue!")
            print("")
    
    def score_keeping(self):
        if self.player_1.score == 2: 
            print("Player 1 has won 2 of 3 rounds!")
            print("")
        else:
            print("Player 2 has won 2 of 3 rounds!")
            print("")

    
    def game_logic(self):
        while self.player_1.score < 2 and self.player_2.score < 2:
            self.player_1.select_gesture()
            self.player_2.select_gesture()
            if self.player_1.gesture_select == self.player_2.gesture_select:
                sleep(.5) 
                print("There has been a tie! Try again.")
                print("")
            elif self.player_1.gesture_select == 0 and self.player_2.gesture_select == 2:
                sleep(.5)
                print("Player one wins")
                print("")
                self.player_1.score += 1
            elif self.player_1.gesture_select == 2 and self.player_2.gesture_select == 1:
                sleep(.5) 
                print("Player one wins")
                print("")
                self.player_1.score += 1
            elif self.player_1.gesture_select == 1 and self.player_2.gesture_select == 0:
                sleep(.5) 
                print("Player one wins")
                print("")
                self.player_1.score += 1
            elif self.player_1.gesture_select == 0 and self.player_2.gesture_select == 3:
                sleep(.5)
                print("") 
                print("Player one wins")
                print("")
                self.player_1.score += 1     
            elif self.player_1.gesture_select == 4 and self.player_2.gesture_select == 2:
                sleep(.5)
                print("Player one wins")
                print("")
                self.player_1.score += 1
            elif self.player_1.gesture_select == 2 and self.player_2.gesture_select == 3:
                sleep(.5) 
                print("Player one wins")
                print("")
                self.player_1.score += 1
            elif self.player_1.gesture_select == 3 and self.player_2.gesture_select == 1:
                sleep(.5) 
                print("Player one wins")
                print("")
                self.player_1.score += 1
            elif self.player_1.gesture_select == 1 and self.player_2.gesture_select == 4:
                sleep(.5) 
                print("Player one wins")
                print("")
                self.player_1.score += 1
            elif self.player_1.gesture_select == 2 and self.player_2.gesture_select == 4:
                sleep(.5) 
                print("Player one wins")
                print("")
                self.player_1.score += 1
            elif self.player_1.gesture_select == 4 and self.player_2.gesture_select == 0:
                sleep(.5) 
                print("Player one wins")
                print("")
                self.player_1.score += 1
            else:
                sleep(.5) 
                print("Player two wins.")
                print("")
                self.player_2.score += 1
        


