import random

# Set up the Q-table with initial values
q_table = {
    ('R', 'R'): 0.5,
    ('R', 'P'): 0.5,
    ('R', 'S'): 0.5,
    ('P', 'R'): 0.5,
    ('P', 'P'): 0.5,
    ('P', 'S'): 0.5,
    ('S', 'R'): 0.5,
    ('S', 'P'): 0.5,
    ('S', 'S'): 0.5,
}

# Define the learning rate and discount factor
learning_rate = 0.1
discount_factor = 0.9

# Define a function to select an action based on the Q-table values
def select_action(state):
    if random.uniform(0, 1) < 0.1:
        # Choose a random action with probability 0.1
        return random.choice(['R', 'P', 'S'])
    else:
        # Choose the action with the highest Q-value for the current state
        return max(q_table[state], key=q_table[state].get)

# Define a function to update the Q-table based on the results of a game
def update_q_table(state, action, reward, next_state):
    old_q_value = q_table[state][action]
    next_max_q_value = max(q_table[next_state].values())
    new_q_value = (1 - learning_rate) * old_q_value + learning_rate * (reward + discount_factor * next_max_q_value)
    q_table[state][action] = new_q_value

# Define a function to play a game against the opponent and update the Q-table
def play_game():
    state = ('R', 'R')
    total_reward = 0

    while True:
        # Choose an action based on the current state
        action = select_action(state)

        # Get the opponent's move
        opponent_move = input("Opponent move (R/P/S): ").upper()

        # Determine the reward based on the outcome of the game
        if action == opponent_move:
            reward = 0
        elif (action == 'R' and opponent_move == 'S') or (action == 'P' and opponent_move == 'R') or (action == 'S' and opponent_move == 'P'):
            reward = 1
        else:
            reward = -1

        # Update the total reward and the Q-table
        total_reward += reward
        next_state = (action, opponent_move)
        update_q_table(state, action, reward, next_state)
        state = next_state

        # Print the current Q-table and total reward
        print(q_table)
        print("Total reward:", total_reward)

        # Ask the player if they want to continue playing
        choice = input("Continue playing? (y/n): ")
        if choice.lower() == 'n':
            break

# Play the game
play_game()
