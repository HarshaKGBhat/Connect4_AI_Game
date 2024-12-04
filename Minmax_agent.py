import math
from ConnectFour import Connect4

class MiniMaxAgent:
    def __init__(self, depth=4):
        self.depth = depth

    def evaluate_board(self, board):
        # Simple heuristic for evaluation
        score = 0
        center_col = [int(i) for i in list(board[:, board.shape[1] // 2])]
        score += center_col.count(1) * 3
        return score

    def minimax(self, game, depth, alpha, beta, maximizing_player):
        winner = game.check_winner()
        if depth == 0 or winner != 0 or game.is_full():
            if winner == 1:
                return (None, 1000000)
            elif winner == 2:
                return (None, -1000000)
            else:
                return (None, self.evaluate_board(game.board))

        if maximizing_player:
            max_eval = -math.inf
            best_col = None
            for col in range(Connect4.COLUMNS):
                if game.is_valid_move(col):
                    temp_game = Connect4()
                    temp_game.board = game.board.copy()
                    temp_game.current_player = game.current_player
                    temp_game.drop_piece(col)
                    eval = self.minimax(temp_game, depth - 1, alpha, beta, False)[1]
                    if eval > max_eval:
                        max_eval = eval
                        best_col = col
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return best_col, max_eval
        else:
            min_eval = math.inf
            best_col = None
            for col in range(Connect4.COLUMNS):
                if game.is_valid_move(col):
                    temp_game = Connect4()
                    temp_game.board = game.board.copy()
                    temp_game.current_player = game.current_player
                    temp_game.drop_piece(col)
                    eval = self.minimax(temp_game, depth - 1, alpha, beta, True)[1]
                    if eval < min_eval:
                        min_eval = eval
                        best_col = col
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return best_col, min_eval

    def get_move(self, game):
        return self.minimax(game, self.depth, -math.inf, math.inf, True)[0]
