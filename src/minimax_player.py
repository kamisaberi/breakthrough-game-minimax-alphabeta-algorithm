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

    def minimax(self, board, move=None, alpha=-math.inf, beta=math.inf, depth=0, MAX=True):
        if depth == self.depth:
            return board.get_scores(board=board.get_board_grid())[0 if MAX else 1], move
        if MAX:
            maxEval = -math.inf
            best_move = None
            for mv in self.get_all_moves(self.player_number):
                brd = copy.deepcopy(board)
                brd.place_piece(move=mv, player_number=0 if MAX else 1)
                evaluation = self.minimax(
                    brd, mv, alpha, beta,  depth+1, not MAX)[0]
                maxEval = max(maxEval, evaluation)
                if maxEval == evaluation:
                    best_move = mv

                if maxEval >= beta:
                    break
                if maxEval > alpha:
                    alpha = maxEval

            return maxEval, best_move
        else:
            minEval = math.inf
            best_move = None
            for mv in self.get_all_moves(int(not bool(self.player_number))):
                brd = copy.deepcopy(board)
                brd.place_piece(move=mv, player_number=0 if MAX else 1)
                evaluation = self.minimax(
                    brd, mv, alpha, beta, depth+1, not MAX)[0]
                minEval = min(minEval, evaluation)
                if minEval == evaluation:
                    best_move = mv

                if minEval <= alpha:
                    break
                if minEval < beta:
                    beta = minEval

            return minEval, best_move

    def get_next_move(self):

        a, b = self.minimax(board=self.board)
        # print(a, b)
        return b

        # TODO: Implement this function based on the minimax algorithm
