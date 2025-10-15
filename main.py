import copy
from agent import QLearningAgent
from train import train_with_random, train_with_oldmodel
from play import play

if __name__ == "__main__":
    agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.1)

    # 1️⃣ 랜덤 상대 학습
    train_with_random(agent, episodes=10000)

    # 2️⃣ self-play 학습
    old_agent = copy.deepcopy(agent)
    train_with_oldmodel(agent, old_agent, episodes=20000)

    # 3️⃣ 학습 후 플레이
    play(agent)