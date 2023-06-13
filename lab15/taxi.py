import gym
import numpy as np

env = gym.make("Taxi-v3", render_mode="human")
observation, info = env.reset(seed=42)

for i in range(30):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()
