class Game:
    def __init__(self):
        self.current_player = 'X'

    def next_ply(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
