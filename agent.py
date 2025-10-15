import random
import numpy as np

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.Q = {}  # {state: [q-values]}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_Qs(self, state):
        if state not in self.Q:
            self.Q[state] = np.zeros(9)
        return self.Q[state]

    def choose_action(self, state, available_actions):
        if random.random() < self.epsilon:
            return random.choice(available_actions)
        q_values = self.get_Qs(state)
        max_q = -999
        best_action = None
        for a in available_actions:
            if q_values[a] > max_q:
                max_q = q_values[a]
                best_action = a
        return best_action

    def update(self, state, action, reward, next_state, done):
        q_values = self.get_Qs(state)
        next_qs = self.get_Qs(next_state)
        if done:
            target = reward
        else:
            target = reward + self.gamma * np.max(next_qs)
        q_values[action] += self.alpha * (target - q_values[action])
