# import game
# from player import Player
# from random_greedy_player import RandomGreedyPlayer
# from random_player import RandomPlayer
# from minimax_player import  MinimaxPlayer


# minimax_game = game.Game(MinimaxPlayer, MinimaxPlayer)
# print(minimax_game.play(True))

import copy
# b= copy.deepcopy(p1.board)
# b.mo
class Student: 
    name = ""
    family = ""
    scores = []
    def __init__(self, name , family , scores) -> None:
        self.name = name
        self.family = family
        self.scores= scores
    def __str__(self) -> str:
        return self.name + " " +  self.family + " " +  str(self.scores)


s1 = Student("ali" , "rezaei" , [15,16,18,19])
s2 = copy.deepcopy(s1)
s2.scores.append(19)
print(s1)
print(s2)