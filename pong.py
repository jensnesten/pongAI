import turtle
import tkinter as tk
import random
from math import cos, sin



wn = turtle.Screen()
wn.title("Pong by @jarlen")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

initial_dx = 4
initial_dy = -4

#score
score_a = 0
score_b = 0


#Ball
ball = turtle.Turtle()
ball.speed(9)
ball.shape("round")
ball.shapesize(stretch_wid=0.5,stretch_len=0.5) #default size is 20px by 20px
ball.color("white")
ball.penup()
ball.goto(0,0)
# Randomize initial direction
ball.dx = initial_dx * cos(random.choice([1, -1]))
ball.dy = initial_dy * sin(random.choice([1, -1]))

new_paddle_height = 1 + (ball.speed - 1) / 2

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=new_paddle_height,stretch_len=0.3) #default size is 20px by 20px
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=new_paddle_height,stretch_len=0.3) #default size is 20px by 20px
paddle_b.penup()
paddle_b.goto(-350,0)

#Initial ball speed



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


#GAME LOOP

# Constants
TOP_BORDER = 290
BOTTOM_BORDER = -290
RIGHT_BORDER = 390
LEFT_BORDER = -390
PADDLE_B_POSITION = 350
PADDLE_A_POSITION = -350
PADDLE_RANGE = 60


def update_ball_position(ball):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

def check_border_collision(ball):
    if ball.ycor() > TOP_BORDER:
        ball.sety(TOP_BORDER)
        ball.dy *= -1
    elif ball.ycor() < BOTTOM_BORDER:
        ball.sety(BOTTOM_BORDER)
        ball.dy *= -1


def check_goal_scored(ball):
    if ball.xcor() > RIGHT_BORDER:
        reset_ball(ball, initial_dx, initial_dy)
        update_score('a')
    elif ball.xcor() < LEFT_BORDER:
        reset_ball(ball, -initial_dx, initial_dy)
        update_score('b')

def reset_ball(ball, dx, dy):
    ball.goto(0, 0)
    start_angle_rad = math.radians(random.randint(1, 360))  
    ball.dx = dx * math.cos(start_angle_rad) * random.choice([1, -1])
    ball.dy = dy * math.sin(start_angle_rad) * random.choice([1, -1])

def update_score(player):
    global score_a, score_b
    if player == 'a':
        score_a += 1
    elif player == 'b':
        score_b += 1
    pen.clear()
    pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier",24,"normal"))

def line_circle_collision(ball, paddle):
    # Get the next position of the ball
    next_ball_x = ball.xcor() + ball.dx
    next_ball_y = ball.ycor() + ball.dy

    # Get the top, bottom, left, and right of the paddle
    paddle_top = paddle.ycor() + new_paddle_height
    paddle_bottom = paddle.ycor() - new_paddle_height
    paddle_left = paddle.xcor() - paddle.width / 2
    paddle_right = paddle.xcor() + paddle.width / 2

    # Check if the line of the ball's movement intersects with the paddle
    if ((ball.ycor() < paddle_top and next_ball_y > paddle_top) or 
        (ball.ycor() > paddle_bottom and next_ball_y < paddle_bottom)) and (
        paddle_left < next_ball_x < paddle_right):
        return True
    else:
        return False

def check_paddle_collision(ball, paddle_a, paddle_b):
    if ball.dx > 0 and line_circle_collision(ball, paddle_b):
        change_ball_direction(ball, "blue")
    elif ball.dx < 0 and line_circle_collision(ball, paddle_a):
        change_ball_direction(ball, "green")

def change_ball_direction(ball, color):
    ball.color(color)
    ball.dx *= -1.1
    ball.dy *= 1.1

while True:
    wn.update()
    update_ball_position(ball)
    if paddle_a_up_key:
        paddle_a_up()
    if paddle_a_down_key:
        paddle_a_down()
    if paddle_b_up_key:
        paddle_b_up()
    if paddle_b_down_key:
        paddle_b_down()
    check_border_collision(ball)
    check_goal_scored(ball)
    check_paddle_collision(ball, paddle_a, paddle_b)

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
    if score_a == 5:
        pen.clear()
        pen.write("Player A wins!", align="center", font=("Courier",24,"normal"))
        ball.goto(0, 0)
        ball.dx *= 0
        ball.dy *= 0
    elif score_b == 5:
        pen.clear()
        pen.write("Player B wins!", align="center", font=("Courier",24,"normal"))
        ball.goto(0, 0)
        ball.dx *= 0
        ball.dy *= 0





