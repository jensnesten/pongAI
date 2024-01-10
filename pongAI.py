import turtle
import os
import tkinter as tk
import random
import random
import math


wn = turtle.Screen()
wn.title("Pong by @jarlen")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

initial_dx = 3
initial_dy = -3

#score
score_a = 0
score_b = 0


#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6,stretch_len=0.3) #default size is 20px by 20px
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6,stretch_len=0.3) #default size is 20px by 20px
paddle_b.penup()
paddle_b.goto(-350,0)

# Create a new turtle for the trail


#ball
ball = turtle.Turtle()
ball.speed(9)
ball.shape("square")
ball.shapesize(stretch_wid=0.5,stretch_len=0.5) #default size is 20px by 20px
ball.color("white")
ball.penup()
ball.goto(0,0)

# Randomize initial direction
ball.dx = initial_dx * random.choice([1, -1])
ball.dy = initial_dy * random.choice([1, -1])

ball.dx = initial_dx * random.choice([1, -1])  # Randomize initial direction
ball.dy = initial_dy * random.choice([1, -1])


start_angle_deg = 23
start_angle_rad = math.radians(start_angle_deg)

initial_dx = 3 * math.cos(start_angle_rad)
initial_dy = 3 * math.sin(start_angle_rad)

# Randomize initial direction
ball.dx = initial_dx * random.choice([1, -1])
ball.dy = initial_dy * random.choice([1, -1])


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #hides the turtle
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24,"normal"))



#functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 5
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 5
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 5
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 5
        paddle_b.sety(y)
paddle_b.goto(350, 0)
#keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up,"w") #when user presses w, call function paddle_a_up
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up") #when user presses w, call function paddle_a_up
wn.onkeypress(paddle_b_down,"Down")

paddle_a_up_key = False
paddle_a_down_key = False
paddle_b_up_key = False
paddle_b_down_key = False

# Functions to set the state of the keys
def paddle_b_up_press():
    global paddle_b_up_key
    paddle_b_up_key = True

def paddle_b_up_release():
    global paddle_b_up_key
    paddle_b_up_key = False

def paddle_b_down_press():
    global paddle_b_down_key
    paddle_b_down_key = True

def paddle_b_down_release():
    global paddle_b_down_key
    paddle_b_down_key = False



# Functions to set the state of the keys
def paddle_a_up_press():
    global paddle_a_up_key
    paddle_a_up_key = True

def paddle_a_up_release():
    global paddle_a_up_key
    paddle_a_up_key = False

def paddle_a_down_press():
    global paddle_a_down_key
    paddle_a_down_key = True

def paddle_a_down_release():
    global paddle_a_down_key
    paddle_a_down_key = False

# Bind the new functions to the key events
wn.listen()
wn.onkeypress(paddle_a_up_press, "w")
wn.onkeyrelease(paddle_a_up_release, "w")
wn.onkeypress(paddle_a_down_press, "s")
wn.onkeyrelease(paddle_a_down_release, "s")
wn.onkeypress(paddle_b_up_press, "Up")
wn.onkeyrelease(paddle_b_up_release, "Up")
wn.onkeypress(paddle_b_down_press, "Down")
wn.onkeyrelease(paddle_b_down_release, "Down")





#main game loop
while True:
    wn.update() #everytime the loop runs, it updates the screen
    #move the ball
    ball.setx(ball.xcor() + ball.dx) #setx is a turtle function
    ball.sety(ball.ycor() + ball.dy)
    if paddle_a_up_key:
        paddle_a_up()
    if paddle_a_down_key:
        paddle_a_down()
    if paddle_b_up_key:
        paddle_b_up()
    if paddle_b_down_key:
        paddle_b_down()
    #border checking
    if ball.ycor() > 290: #top border
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290: #bottom border
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390: #right border
        ball.goto(0,0)
        ball.dx = initial_dx * random.choice([1, -1]) # Reset ball speed
        ball.dy = initial_dy * random.choice([1, -1]) # Reset ball speed
        score_a += 1
        pen.clear() #clears the previous score
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))
    if ball.xcor() < -390: #left border
        ball.goto(0,0)
        ball.dx = -initial_dx * random.choice([1, -1])  # Reset ball speed
        ball.dy = initial_dy * random.choice([1, -1])  # Reset ball speed
        score_b += 1
        pen.clear() #clears the previous score
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))
    #paddle and ball collisions
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 65 > ball.ycor() > paddle_b.ycor() - 65):
        ball.color("blue")
        ball.dx *= -1
        ball.dx *= 1.05
        ball.dy *= 1.05
    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 65 > ball.ycor() > paddle_a.ycor() - 65):
        ball.color("red")
        ball.dx *= -1
        ball.dx *= 1.05  
        ball.dy *= 1.05

    def predict_ball_position(ball):
    # Calculate how much the ball will move horizontally until it reaches the paddle
        distance_to_paddle = 350 - abs(ball.xcor())

    # Calculate how much the ball will move vertically in this time
        future_ball_movement = distance_to_paddle * ball.dy / abs(ball.dx)

    # Predict the future y-position of the ball
        future_ball_y = ball.ycor() + future_ball_movement
        
        if abs(future_ball_y) > 290:
        # Calculate how much the ball will move after bouncing
            bounce = abs(future_ball_y) - 290
            # If the ball is moving up, subtract the bounce from the top of the screen
            if future_ball_y > 0:
                future_ball_y = 290 - bounce
            # If the ball is moving down, add the bounce to the bottom of the screen
            else:
                future_ball_y = -290 + bounce

        return future_ball_y
        

        # AI Player
    if ball.dx > 0:  # ball is moving towards paddle B
        future_ball_y = predict_ball_position(ball)
        if paddle_b.ycor() < future_ball_y and paddle_b.ycor() < 250:  # Add boundary condition
            paddle_b.sety(paddle_b.ycor() + 8)
        elif paddle_b.ycor() > future_ball_y and paddle_b.ycor() > -250:  # Add boundary condition
            paddle_b.sety(paddle_b.ycor() - 8)
    elif ball.dx < 0:  # ball is moving towards paddle A
        future_ball_y = predict_ball_position(ball)
        if paddle_a.ycor() < future_ball_y and paddle_a.ycor() < 250:  # Add boundary condition
            paddle_a.sety(paddle_a.ycor() + 8)
        elif paddle_a.ycor() > future_ball_y and paddle_a.ycor() > -250:  # Add boundary condition
            paddle_a.sety(paddle_a.ycor() - 8)

    # Missed ball paddle_b
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= 1
    # Missed ball paddle_a
    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= 1

   
    #winning condition
    if score_a == 10:
        pen.clear()
        pen.write("Player A wins!", align="center", font=("Courier",24,"normal"))
        ball.goto(0, 0)
        ball.dx *= 0
        ball.dy *= 0
    if score_b == 10:
        pen.clear()
        pen.write("Player B wins!", align="center", font=("Courier",24,"normal"))
        ball.goto(0, 0)
        ball.dx *= 0
        ball.dy *= 0





