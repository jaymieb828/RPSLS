

from human import Human
from ai import AI


player_1 = Human()
player_2 = AI()

class Game:
    def __init__(self) -> None:
        pass
    
    def choose_gestures(self):
        player_1.select_gesture()
        player_2.select_gesture()
        print("Let's Play!")

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
        while player_1.score <=2:
            if player_1.gesture_select == 0 and player_2.gesture_select == 1:
                print("Player 1 wins!")

    def run_game(self):
        self.choose_gestures()
        self.game_logic()
        self.score_keeping()
        

