from ConnectFour import Connect4
from Minmax_agent import MiniMaxAgent
from Qlearning_agent import QLearningAgent

def human_vs_agent(agent_type='minimax', depth=4):
    game = Connect4()
    minimax_agent = MiniMaxAgent(depth=depth)
    qlearning_agent = QLearningAgent()
    qlearning_agent.train(game, episodes=500)

    agent = minimax_agent if agent_type == 'minimax' else qlearning_agent

    while not game.check_winner() and not game.is_full():
        print("\nCurrent Board:")
        print(game.board)
        if game.current_player == 1:
            col = int(input("Your move (0-6): "))
            if not game.is_valid_move(col):
                print("Invalid move. Try again.")
                continue
        else:
            col = agent.get_move(game) if agent_type == 'minimax' else agent.choose_action(game)
            print(f"AI chose column: {col}")

        game.drop_piece(col)
        game.switch_player()

    winner = game.check_winner()
    if winner == 1:
        print("Congratulations! You won!")
    elif winner == 2:
        print("AI wins. Better luck next time!")
    else:
        print("It's a draw!")
    print("Final Board:")
    print(game.board)
