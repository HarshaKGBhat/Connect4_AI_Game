import numpy as np

class Connect4:
    ROWS = 6
    COLUMNS = 7

    def __init__(self):
        self.board = np.zeros((self.ROWS, self.COLUMNS), dtype=int)
        self.current_player = 1

    def drop_piece(self, column):
        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                return True
        return False

    def is_valid_move(self, column):
        return self.board[0][column] == 0

    def switch_player(self):
        self.current_player = 3 - self.current_player

    def check_winner(self):
        # Check all directions for a win
        for row in range(self.ROWS):
            for col in range(self.COLUMNS - 3):
                if self.check_line(row, col, 0, 1):
                    return self.board[row][col]

        for row in range(self.ROWS - 3):
            for col in range(self.COLUMNS):
                if self.check_line(row, col, 1, 0):
                    return self.board[row][col]

        for row in range(self.ROWS - 3):
            for col in range(self.COLUMNS - 3):
                if self.check_line(row, col, 1, 1):
                    return self.board[row][col]

        for row in range(3, self.ROWS):
            for col in range(self.COLUMNS - 3):
                if self.check_line(row, col, -1, 1):
                    return self.board[row][col]
        return 0

    def check_line(self, row, col, delta_row, delta_col):
        piece = self.board[row][col]
        if piece == 0:
            return False
        for i in range(1, 4):
            if self.board[row + i * delta_row][col + i * delta_col] != piece:
                return False
        return True

    def is_full(self):
        return all(self.board[0, col] != 0 for col in range(self.COLUMNS))

    def reset(self):
        self.board = np.zeros((self.ROWS, self.COLUMNS), dtype=int)
        self.current_player = 1
