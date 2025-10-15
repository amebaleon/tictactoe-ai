from env import TicTacToe

def print_board(board):
    for i in range(3):
        print(' | '.join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def play(agent):
    env = TicTacToe()
    state = env.reset()
    while True:
        print_board(env.board)
        
        # AI 차례
        available = env.available_actions()
        action = agent.choose_action(state, available)
        env.make_move(action, 'X')
        print_board(env.board)
        if env.current_winner == 'X':
            print("AI wins!")
            break
        elif env.is_full():
            print("Draw.")
            break

        # 사용자 차례
        available = env.available_actions()
        while True:
            try:
                opp = int(input(f"Your move (0-8), available: {available}: "))
                if opp in available:
                    break
                else:
                    print("Invalid move! Try again.")
            except:
                print("Invalid input! Enter a number between 0-8.")

        env.make_move(opp, 'O')
        if env.current_winner == 'O':
            print("You win!")
            break
        elif env.is_full():
            print("Draw.")
            break

        state = env.get_state()
