from othello_board import OthelloBoard


class Game:
    def __init__(self):
        self.current_player = 'X'

    def next_ply(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def set_current_player(self, player):
        self.current_player = player

    def is_terminal(self, board):
        return not board.has_legal_moves_remaining('X') and not board.has_legal_moves_remaining('O')

    def utility(self, board):
        return board.count_score('X') - board.count_score('O')

    def actions(self, board):
        actions = []
        num_cols = board.get_num_cols()
        num_rows = board.get_num_rows()
        for col in range(0, num_cols):
            for row in range(0, num_rows):
                if board.is_legal_move(col, row, self.current_player):
                    actions.append((col, row))
        return actions

    def successor(self, board):
        successors = []
        for action in self.actions(board):
            col = action[0]
            row = action[1]
            new_board = board.clone_of_board()
            new_board.play_move(col, row, self.current_player)  # Generate a successor - a potential next move
            successors.append(new_board)
        return successors
