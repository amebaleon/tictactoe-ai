import random

class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [' '] * 9
        self.current_winner = None
        return self.get_state()

    def get_state(self):
        return ''.join(self.board)

    def available_actions(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def make_move(self, position, letter):
        if self.board[position] == ' ':
            self.board[position] = letter
            if self.check_winner(letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, letter):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for combo in wins:
            if all(self.board[i] == letter for i in combo):
                return True
        return False

    def is_full(self):
        return ' ' not in self.board
