import gym

env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset(seed=42)

for i in range(300):
    action = 0
    print("Akcja nr ", i, ": ", action)
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()
