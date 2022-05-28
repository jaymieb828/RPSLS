

from human import Human
from ai import AI
from time import sleep

player_1 = Human()
player_2 = AI()
    
class Game:
    def __init__(self) -> None:
        self.player_1 = Human()
        self.player_2 = AI()
        
        
    def run_game(self):
        self.game_logic()
        self.score_keeping()
    
    def score_keeping(self):
        if self.player_1.score == 2:
            print("Player 1 has won 2 of 3 rounds!")
        else:
            print("Player 2 has won 2 of 3 rounds!")

    
    def game_logic(self):
        while self.player_1.score < 2 and self.player_2.score < 2:
            self.player_1.select_gesture()
            self.player_2.select_gesture()
            if self.player_1.gesture == self.player_2.gesture:
                print("There has been a tie! Try again.")
            elif self.player_1.gesture == 0 and self.player_2.gesture == 2:
                print("Player one wins")
                self.player_1.score += 1
            elif self.player_1.gesture == 2 and self.player_2.gesture == 1:
                print("Player one wins")
                self.player_1.score += 1
            elif self.player_1.gesture == 1 and self.player_2.gesture == 0:
                print("Player one wins")
                self.player_1.score += 1
            elif self.player_1.gesture == 0 and self.player_2.gesture == 3:
                print("Player one wins")
                self.player_1.score += 1     
            elif self.player_1.gesture == 4 and self.player_2.gesture == 2:
                print("Player one wins")
                self.player_1.score += 1
            elif self.player_1.gesture == 2 and self.player_2.gesture == 3:
                print("Player one wins")
                self.player_1.score += 1
            elif self.player_1.gesture == 3 and self.player_2.gesture == 1:
                print("Player one wins")
                self.player_1.score += 1
            elif self.player_1.gesture == 1 and self.player_2.gesture == 4:
                print("Player one wins")
                self.player_1.score += 1
            elif self.player_1.gesture == 2 and self.player_2.gesture == 4:
                print("Player one wins")
                self.player_1.score += 1
            elif self.player_1.gesture == 4 and self.player_2.gesture == 0:
                print("Player one wins")
                self.player_1.score += 1
            else:
                print("Player two wins.")
                self.player_2.score += 1
        


