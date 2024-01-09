#we make the pong environment
import turtle
import os
import tkinter as tk
import random
from turtle import Turtle, Screen
import gym
from gym import spaces
import numpy as np


class PongEnvironment(gym.Env):
    def __init__(self):
        super(PongEnvironment, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions, Box for continuous
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=600, shape=(4,))

        # Initialize the Pong game
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.paddle_a = Turtle()
        self.paddle_a.speed(0) 
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        self.paddle_a.shapesize(stretch_wid=5,stretch_len=0.3)
        # TODO: Set the initial position of paddle_a

    def step(self, action):
        # Execute the action
        # TODO: 
        
        #we Update the game state based on the action
        

        # TODO: Calculate the reward
        
        # TODO: Determine whether the game is over
        # Return the new state, the reward, and whether the game is over
        pass

    def reset(self):
        # Reset the game
        # TODO: Reset the game to its initial state
        # Return the initial state
        pass

    def render(self, mode='human'):
        # Render the game
        # TODO: Update the screen with the current game state
        pass