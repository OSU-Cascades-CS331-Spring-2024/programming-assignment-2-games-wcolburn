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

    def max_value(self, board):
        if self.game.is_terminal(board):
            self.game.next_ply()
            return self.game.utility(board), None

        value = float('-inf')
        move = None
        states = self.game.successor(board)
        actions = self.game.actions(board)
        for i in range(len(actions)):
            v2, a2 = self.min_value(states[i])
            if v2 > value:
                value, move = v2, actions[i]
        self.game.next_ply()
        return value, move

    def min_value(self, board):
        if self.game.is_terminal(board):
            self.game.next_ply()
            return self.game.utility(board), None

        value = float('inf')
        move = None
        states = self.game.successor(board)
        actions = self.game.actions(board)
        for i in range(len(actions)):
            v2, a2 = self.max_value(states[i])
            if v2 < value:
                value, move = v2, actions[i]
        self.game.next_ply()
        return value, move

    def get_move(self, board):
        self.game.set_current_player(self.symbol)
        if self.symbol == 'X':
            value, move = self.max_value(board)
        else:
            value, move = self.min_value(board)
        return move
