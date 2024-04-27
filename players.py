'''
    Defines Player class, and subclasses Human and Minimax Player.
'''


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

    def is_terminal(self, board):
        return not board.has_legal_moves_remaining(self.symbol) and not board.has_legal_moves_remaining(self.oppSym)

    def utility(self, board):
        return board.count_score('X') - board.count_score('O')

    def successor(self, board):
        new_board = board.clone_of_board
        for col in board.get_num_cols:
            for row in board.get_num_rows:
                if board.is_legal_move(col, row)


    def max_value(self, board):
        if self.is_terminal(board):
            return self.utility(board), None

        value = float('-inf')
        for result in self.successor(board):
            v2, a2 = self.min_value(result)

    def min_value(self, board):
        return None, None

    def get_move(self, board):
        if self.symbol == 'X':
            value, move = self.max_value(board)
        else:
            value, move = self.min_value(board)
        return move
