'''
    Defines Player class, and subclasses Human and Minimax Player.
'''
from game import Game


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    # PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol

    # parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)

    # PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
        self.game = Game()

    def calc_depth_limit(self, board):
        return (board.get_num_cols() + board.get_num_rows()) / 4.5

    def max_value(self, board, depth):
        if self.game.is_terminal(board) or depth > self.calc_depth_limit(board):
            return self.game.utility(board), None

        value = float('-inf')
        move = None
        states = self.game.successor(board)
        actions = self.game.actions(board)
        for i in range(len(actions)):
            v2, a2 = self.min_value(states[i], depth + 1)
            if v2 > value:
                value, move = v2, actions[i]
        self.game.next_ply()
        return value, move

    def min_value(self, board, depth):
        if self.game.is_terminal(board) or depth > self.calc_depth_limit(board):
            return self.game.utility(board), None

        value = float('inf')
        move = None
        states = self.game.successor(board)
        actions = self.game.actions(board)
        for i in range(len(actions)):
            v2, a2 = self.max_value(states[i], depth + 1)
            if v2 < value:
                value, move = v2, actions[i]
        self.game.next_ply()
        return value, move

    def get_move(self, board):
        self.game.set_current_player(self.symbol)
        depth = 0
        if self.symbol == 'X':
            value, move = self.max_value(board, depth)
        else:
            value, move = self.min_value(board, depth)
        return move

