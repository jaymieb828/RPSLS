

from human import Human
from ai import AI


player_1 = Human()
player_2 = AI()
    
class Game:
    def __init__(self) -> None:
        self.player_1 = Human()
        self.player_2 = AI()
        self.score = 0
        self.gestures = None
        
    def run_game(self):
        self.choose_gestures()
        self.game_logic()
        self.score_keeping()
    
    def choose_gestures(self):
        player_1.select_gesture()
        player_2.select_gesture()
        

    def score_keeping(self):
        score = 0
        self.winner = 2
        if self.player_1 == score == self.winner:
            self.player_1 = self.winner
            print("Player 1 wins!")
        else:
            self.player_2 = self.winner
            print("Player 2 wins!")

    
    def game_logic(self):
        while self.score <= 2:
            if self.player_1.select_gesture == 0  and self.player_2.select_gesture == 1:
                print("Player one wins") 
                return(self.player_1.score + 1)
            elif self.player_1.select_gesture == 1  and self.player_2.select_gesture == 2:
                print("Player one wins")
                return(self.player_1.score + 1)
            elif self.player_1.select_gesture == 2  and self.player_2.select_gesture == 0:
                print("Player one wins")
                return(self.player_1.score + 1)
            elif self.player_1.select_gesture == 0  and self.player_2.select_gesture == 3:
                print("Player one wins")
                return(self.player_1.score + 1)       
            elif self.player_1.select_gesture == 3  and self.player_2.select_gesture == 4:
                print("Player one wins")
                return(self.player_1.score + 1)
            elif self.player_1.select_gesture == 4  and self.player_2.select_gesture == 1:
                print("Player one wins")
                return(self.player_1.score + 1)
            elif self.player_1.select_gesture == 1  and self.player_2.select_gesture == 3:
                print("Player one wins")
                return(self.player_1.score + 1)
            elif self.player_1.select_gesture == 3  and self.player_2.select_gesture == 2:
                print("Player one wins")
                return(self.player_1.score + 1)
            elif self.player_1.select_gesture == 2  and self.player_2.select_gesture == 4:
                print("Player one wins")
                return(self.player_1.score + 1)
            elif self.player_1.select_gesture == 4  and self.player_2.select_gesture == 0:
                print("Player one wins")
                return(self.player_1.score + 1)
            elif player_1.select_gesture == player_2.select_gesture:
                print("There has been a tie! Try again.")
                return(self.score == 0)
            else:
                print("Player two wins.")
                return(self.score +1)


