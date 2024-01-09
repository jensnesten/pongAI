import torch
import torch.nn as nn
import torch.optim as optim
from pong import paddle_a_up_press, paddle_a_down_press, paddle_a_down_release, paddle_a_up_release, paddle_b_up_press, paddle_b_down_press, paddle_b_down_release, paddle_b_up_release
import pong
from torch.utils.tensorboard import SummaryWriter
from pongenv import PongEnvironment



# Define your model
class PongModel(nn.Module):
    def __init__(self):
        super(PongModel, self).__init__()
        self.fc = nn.Linear(6, 2)  # 6 inputs (paddle A position, paddle B position, ball position, ball direction), 2 outputs (move paddle A up, move paddle A down)

    def forward(self, x):
        return self.fc(x)
    

model = PongModel()
optimizer = optim.SGD(model.parameters(), lr=0.01)


def reward_function(game_state, action):
    # Define your reward function here
    paddle_a_pos, paddle_b_pos, ball_pos, ball_dir = game_state
    if action == 0:
        paddle_a_pos += 20
    else:
        paddle_a_pos -= 20
    if paddle_a_pos < 0:
        paddle_a_pos = 0
    if paddle_a_pos > 240:
        paddle_a_pos = 240
    if paddle_b_pos < 0:
        paddle_b_pos = 0
    if paddle_b_pos > 240:
        paddle_b_pos = 240
    if ball_pos[1] < 0:
        ball_pos[1] = 0
    if ball_pos[1] > 240:
        ball_pos[1] = 240
    if ball_pos[0] < 0:
        ball_pos[0] = 0
    if ball_pos[0] > 240:
        ball_pos[0] = 240

    if ball_pos[0] < 20:
        if ball_pos[1] > paddle_a_pos and ball_pos[1] < paddle_a_pos + 60:
            return 1
        else:
            return -1
    else:
        return 0

# Define your action selection function
def select_action(state, model, epsilon):
    if torch.rand(1).item() < epsilon:
        return torch.randint(2, (1,)).item()  # Random action
    else:
        with torch.no_grad():
            return model(state).argmax().item()  # Best action according to the model


# Define your training function
def train_model(state, action, reward, next_state, model, optimizer):
    
    # Convert state and next_state to 2D tensors
    state = state.unsqueeze(0)
    next_state = next_state.unsqueeze(0)
    # Compute the target Q-value
    with torch.no_grad():
        target = reward + model(next_state).max(1)[0]
    # Get the predicted Q-value from the model
    prediction = model(state)[0, action]
    # Compute the loss
    loss = nn.functional.mse_loss(prediction, target)
    # Zero gradients
    optimizer.zero_grad()
    # Backpropagate the loss
    loss.backward()
    # Update the weights
    optimizer.step()

writer = SummaryWriter()

num_episodes = 10  # Define the number of episodes
env = PongEnvironment()  # Define the environment
max_timesteps_per_episode = 100  # Define the maximum number of timesteps per episode


for episode in range(num_episodes):
    # Reset the environment and get the initial state
    state = env.reset()
    total_reward = 0

    for t in range(max_timesteps_per_episode):
        # Select and perform an action
        action = select_action(state)
        next_state, reward, done, _ = env.step(action)

        # Train the model
        train_model(state, action, reward, next_state, model, optimizer)

        # Update the total reward
        total_reward += reward

        # Move to the next state
        state = next_state

        # End the episode if done
        if done:
            break
        print(f"Episode: {episode}, Total reward: {total_reward}, Epsilon: {epsilon}")
            

    # Log the total reward
    writer.add_scalar('Total reward', total_reward, episode)

# Close the SummaryWriter at the end of training
writer.close()


def get_paddle_a_pos():
    return pong.paddle_a.ycor()

def get_paddle_b_pos():
    return pong.paddle_b.ycor()

def get_ball_pos():
    return (pong.ball.xcor(), pong.ball.ycor())

def get_ball_dir():
    return (pong.ball.dx, pong.ball.dy)

def perform_action(game_state, action):
    if action == 0:
        paddle_a_up_press()
    else:
        paddle_a_down_press()

    pong.main()

    paddle_a_up_release()
    paddle_a_down_release()

    return [get_paddle_a_pos(), get_paddle_b_pos(), get_ball_pos(), get_ball_dir()], reward_function(game_state, action)


# In your game loop
epsilon = 1.0  # Start with a high epsilon
epsilon_min = 0.01  # The minimum value epsilon can reach
epsilon_decay = 0.99  # The multiplicative factor to decrease epsilon

while True:
    # Get game state
    paddle_a_pos = get_paddle_a_pos()  
    paddle_b_pos = get_paddle_b_pos()  
    ball_pos = get_ball_pos()  
    ball_dir = get_ball_dir()

    game_state = [paddle_a_pos, paddle_b_pos, ball_pos, ball_dir]
    # Convert game state to tensor
    game_state = torch.tensor(game_state, dtype=torch.float)
    # Select action
    action = select_action(game_state, model, epsilon)
    # Perform action and get new game state and reward
    next_game_state, reward = perform_action(game_state, action)
    # Convert next game state to tensor
    next_game_state = torch.tensor(next_game_state, dtype=torch.float)
    # Train model
    train_model(game_state, action, reward, next_game_state, model, optimizer)
    # Update game state
    game_state = next_game_state

    # Decay epsilon
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay