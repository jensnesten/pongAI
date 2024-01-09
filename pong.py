#we are going to make a pong game

import turtle
import os
import tkinter as tk
import random


wn = turtle.Screen()
wn.title("Pong by @Karthik")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=0.2) #default size is 20px by 20px
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=0.2) #default size is 20px by 20px
paddle_b.penup()
paddle_b.goto(-350,0)

#ball
ball = turtle.Turtle()
ball.speed(9)
ball.shape("square")
ball.shapesize(stretch_wid=0.5,stretch_len=0.5) #default size is 20px by 20px
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2 * random.choice([1, -1])  # Randomize initial direction
ball.dy = 2 * random.choice([1, -1])

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
    wn.update()

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
        os.system("afplay bounce.wav&") #& allows the sound to play while the game is running

    if ball.ycor() < -290: #bottom border
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&") #& allows the sound to play while the game is running

    if ball.xcor() > 390: #right border
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear() #clears the previous score
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

    if ball.xcor() < -390: #left border
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear() #clears the previous score
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

    #paddle and ball collisions
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.color("blue")
        ball.dx *= -1

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.color("red")
        ball.dx *= -1

    # Missed ball paddle_b
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1

    # Missed ball paddle_a
    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1




