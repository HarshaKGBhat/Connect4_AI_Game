import numpy as np
import random
from ConnectFour import Connect4

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.q_table = {}  # Q-values stored as {(state, action): value}

    def get_state(self, game):
        return tuple(map(tuple, game.board))  # Represent the board as a tuple

    def choose_action(self, game):
        state = self.get_state(game)
        if random.uniform(0, 1) < self.epsilon:
            # Exploration: Random action
            valid_actions = [col for col in range(Connect4.COLUMNS) if game.is_valid_move(col)]
            return random.choice(valid_actions)
        else:
            # Exploitation: Best known action
            q_values = {col: self.q_table.get((state, col), 0) for col in range(Connect4.COLUMNS)}
            valid_actions = {col: q for col, q in q_values.items() if game.is_valid_move(col)}
            if not valid_actions:
                return random.choice(range(Connect4.COLUMNS))  # Default to random if no valid action
            return max(valid_actions, key=valid_actions.get)

    def update_q_value(self, state, action, reward, next_state):
        old_value = self.q_table.get((state, action), 0)
        future_rewards = [self.q_table.get((next_state, col), 0) for col in range(Connect4.COLUMNS)]
        best_future = max(future_rewards) if future_rewards else 0
        self.q_table[(state, action)] = old_value + self.alpha * (reward + self.gamma * best_future - old_value)

    def train(self, game, episodes=1000):
        for _ in range(episodes):
            game.reset()
            state = self.get_state(game)
            while not game.check_winner() and not game.is_full():
                action = self.choose_action(game)
                valid_move = game.drop_piece(action)
                if not valid_move:
                    continue
                next_state = self.get_state(game)
                reward = 0
                if game.check_winner() == game.current_player:
                    reward = 1
                elif game.is_full():
                    reward = 0.5  # Draw
                self.update_q_value(state, action, reward, next_state)
                state = next_state
                game.switch_player()
