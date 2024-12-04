from ConnectFour import Connect4
from Minmax_agent import MiniMaxAgent
from Qlearning_agent import QLearningAgent

def qlearning_vs_minimax():
    game = Connect4()
    minimax_agent = MiniMaxAgent(depth=4)
    qlearning_agent = QLearningAgent()
    qlearning_agent.train(game, episodes=500)

    print("\nStarting Q-Learning vs MiniMax...")
    while not game.check_winner() and not game.is_full():
        if game.current_player == 1:
            col = qlearning_agent.choose_action(game)
        else:
            col = minimax_agent.get_move(game)

        game.drop_piece(col)
        game.switch_player()

    winner = game.check_winner()
    print("\nGame Over!")
    print(game.board)
    if winner == 1:
        print("Q-Learning Agent Wins!")
    elif winner == 2:
        print("MiniMax Agent Wins!")
    else:
        print("It's a draw!")
    return winner

def human_vs_human():
    game = Connect4()
    print("\nStarting Human vs Human...")
    while not game.check_winner() and not game.is_full():
        print("\nCurrent Board:")
        print(game.board)
        try:
            col = int(input(f"Player {game.current_player}'s move (0-6): "))
            if col < 0 or col >= Connect4.COLUMNS:
                print("Invalid move. Please enter a column between 0 and 6.")
                continue
            if not game.is_valid_move(col):
                print("Invalid move! The column is filled. Try again with a different column.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")
            continue

        game.drop_piece(col)
        game.switch_player()

    winner = game.check_winner()
    print("\nGame Over!")
    print(game.board)
    if winner:
        print(f"Player {winner} Wins!")
    else:
        print("It's a draw!")
    return winner

def qlearning_vs_human():
    game = Connect4()
    qlearning_agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.1)

    print("\nStarting Q-Learning vs Human...")

    while not game.check_winner() and not game.is_full():
        print("\nCurrent Board:")
        print(game.board)

        if game.current_player == 1:
            # Q-Learning agent's turn (always plays first)
            col = qlearning_agent.choose_action(game)
            print(f"Q-Learning Agent chose column: {col}")
        else:
            # Human's turn
            try:
                col = int(input("Your move (0-6): "))
                if col < 0 or col >= Connect4.COLUMNS:
                    print("Invalid move. Please enter a column between 0 and 6.")
                    continue
                if not game.is_valid_move(col):
                    print("Invalid move! The column is filled. Try again with a different column.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 6.")
                continue

        game.drop_piece(col)
        game.switch_player()

    winner = game.check_winner()
    print("\nGame Over!")
    print(game.board)
    if winner == 1:
        print("Q-Learning Agent Wins!")
    elif winner == 2:
        print("You Win!")
    else:
        print("It's a draw!")
    return winner

def minimax_vs_human():
    game = Connect4()
    minimax_agent = MiniMaxAgent(depth=4)

    print("\nStarting MiniMax vs Human...")
    while not game.check_winner() and not game.is_full():
        print("\nCurrent Board:")
        print(game.board)
        if game.current_player == 1:
            col = minimax_agent.get_move(game)
            print(f"MiniMax Agent chose column: {col}")
        else:
            try:
                col = int(input("Your move (0-6): "))
                if col < 0 or col >= Connect4.COLUMNS:
                    print("Invalid move. Please enter a column between 0 and 6.")
                    continue
                if not game.is_valid_move(col):
                    print("Invalid move! The column is filled. Try again with a different column.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 6.")
                continue

        game.drop_piece(col)
        game.switch_player()

    winner = game.check_winner()
    print("\nGame Over!")
    print(game.board)
    if winner == 1:
        print("MiniMax Agent Wins!")
    elif winner == 2:
        print("You Win!")
    else:
        print("It's a draw!")
    return winner

def play_tournament():
    print("\nTournament Mode!")
    print("Select tournament type:")
    print("1. Human vs Human")
    print("2. Q-Learning vs MiniMax")
    print("3. Q-Learning vs Human")
    print("4. MiniMax vs Human")

    choice = input("Enter your choice: ")
    
    num_games = int(input("Enter number of games in the tournament: "))

    if num_games <= 0:
        print("Atleast 1 game need to play!!")
        return

    results = {"Player 1 Wins": 0, "Player 2 Wins": 0, "Draws": 0}

    for game_num in range(1, num_games + 1):
        print(f"\nGame {game_num} of {num_games}")
        if choice == '1':
            winner = human_vs_human()
        elif choice == '2':
            winner = qlearning_vs_minimax()
        elif choice == '3':
            winner = qlearning_vs_human()
        elif choice == '4':
            winner = minimax_vs_human()
        else:
            print("Invalid choice.")
            return

        # Update results
        if winner == 1:
            results["Player 1 Wins"] += 1
        elif winner == 2:
            results["Player 2 Wins"] += 1
        else:
            results["Draws"] += 1

    # Display tournament results
    print("\nTournament Results:")
    for result, count in results.items():
        print(f"{result}: {count}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Q-Learning vs MiniMax")
        print("2. Human vs Human")
        print("3. Q-Learning vs Human")
        print("4. MiniMax vs Human")
        print("5. Play Tournament")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            qlearning_vs_minimax()
        elif choice == '2':
            human_vs_human()
        elif choice == '3':
            qlearning_vs_human()
        elif choice == '4':
            minimax_vs_human()
        elif choice == '5':
            play_tournament()
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
