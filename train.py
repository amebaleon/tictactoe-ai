import pickle
import random
from env import TicTacToe

def train_with_random(agent, episodes=50000):
    env = TicTacToe()
    for ep in range(episodes):
        state = env.reset()
        done = False
        while not done:
            available = env.available_actions()
            action = agent.choose_action(state, available)
            env.make_move(action, 'X')

            if env.current_winner == 'X':
                agent.update(state, action, 1, env.get_state(), True)
                done = True
                break
            elif env.is_full():
                agent.update(state, action, 0, env.get_state(), True)
                done = True
                break

            opp_action = random.choice(env.available_actions())
            env.make_move(opp_action, 'O')

            if env.current_winner == 'O':
                agent.update(state, action, -1, env.get_state(), True)
                done = True
            elif env.is_full():
                agent.update(state, action, 0, env.get_state(), True)
                done = True
            else:
                next_state = env.get_state()
                agent.update(state, action, 0, next_state, False)
                state = next_state

        if (ep+1) % 5000 == 0:
            print(f"[Random] Episode {ep+1}/{episodes}")

    with open("q_tables/q_table_random.pkl", "wb") as f:
        pickle.dump(agent.Q, f)
    print("Random phase training complete, Q-table saved as q_tables/q_table_random.pkl")

def train_with_oldmodel(agent, old_agent, episodes=50000):
    env = TicTacToe()
    for ep in range(episodes):
        state = env.reset()
        done = False
        while not done:
            available = env.available_actions()
            action = agent.choose_action(state, available)
            env.make_move(action, 'X')

            if env.current_winner == 'X':
                agent.update(state, action, 1, env.get_state(), True)
                done = True
                break
            elif env.is_full():
                agent.update(state, action, 0, env.get_state(), True)
                done = True
                break

            # 이전 모델 상대
            opp_state = env.get_state()
            available = env.available_actions()
            opp_action = old_agent.choose_action(opp_state, available)
            env.make_move(opp_action, 'O')

            if env.current_winner == 'O':
                agent.update(state, action, -1, env.get_state(), True)
                done = True
            elif env.is_full():
                agent.update(state, action, 0, env.get_state(), True)
                done = True
            else:
                next_state = env.get_state()
                agent.update(state, action, 0, next_state, False)
                state = next_state

        if (ep+1) % 5000 == 0:
            print(f"[Self-play] Episode {ep+1}/{episodes}")

    with open("q_tables/q_table_selfplay.pkl", "wb") as f:
        pickle.dump(agent.Q, f)
    print("Self-play training complete, Q-table saved as q_tables/q_table_selfplay.pkl")
