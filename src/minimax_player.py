import copy
import random
from player import Player
import time
import math


class MinimaxPlayer(Player):
    def __init__(self, player_number, board, depth=3):
        super().__init__(player_number, board)
        self.depth = depth

    def get_all_moves(self, palyer_number):
        moves = []
        range_n = 0, self.board.get_n()
        step = 1
        if self.player_number == 0:
            range_n = self.board.get_n() - 1, -1
            step = -1
        for i in range(range_n[0], range_n[1], step):
            for j in range(range_n[0], range_n[1], step):
                if self.board.get_board_grid()[i][j] == palyer_number:
                    for direction in self.board.get_possible_directions(palyer_number):
                        move = (i, j), (i + direction[0], j + direction[1])
                        self.board.start_imagination()
                        if self.board.is_move_valid(self.board.get_imaginary_board(), move, palyer_number):
                            moves.append(move)
        return moves

    def minimax(self, pos=None,  depth=0, MAX=True):
        # print(depth)
        if depth == self.depth:
            brd = copy.deepcopy(self.board)
            brd.place_piece(move=pos, player_number=0 if MAX else 1)
            return brd.get_scores(board=brd.get_board_grid())[0 if MAX else 1], pos

        if MAX:
            maxEval = -math.inf
            best_move = None
            for move in self.get_all_moves(self.player_number):
                # print(move)
                evaluation = self.minimax(move, depth+1, True)[0]
                # print(move, evaluation)
                maxEval = max(maxEval, evaluation)
                # print(move, evaluation, maxEval)
                if maxEval == evaluation:
                    best_move = move
            # print(maxEval, best_move)
            return maxEval, best_move
        else:
            minEval = math.inf
            best_move = None
            for move in self.get_all_moves(int(not bool(self.player_number))):
                evaluation = self.minimax(move, depth+1, False)[0]
                minEval = min(minEval, evaluation)
                if minEval == evaluation:
                    best_move = move
            return minEval, best_move

    def get_next_move(self):

        # moves = self.get_all_moves(self.player_number)
        # for move in moves:
        #     a, b = self.minimax()
        # self.minimax(self.board , )
        # if self.player_number == 0:
        #     pass
        # else:
        #     pass
        a, b = self.minimax()
        print(a, b)
        return b

        # TODO: Implement this function based on the minimax algorithm
