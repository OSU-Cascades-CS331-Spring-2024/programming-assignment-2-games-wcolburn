class Game:
    def __init__(self):
        self.current_player = 'X'

    def next_ply(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def successor(self, board):
        successors = []
        for col in board.get_num_cols:
            for row in board.get_num_rows:
                if board.is_legal_move(col, row, self.current_player):
                    new_board = board.clone_of_board
                    new_board.play_move(col, row, self.current_player)  # Generate a successor - a potential next move
                    successors.append(new_board)
        return successors
