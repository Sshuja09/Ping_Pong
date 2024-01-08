import turtle
import random

# Set up the window
window = turtle.Screen()
window.title("PONG GAME!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Initialize scores
score_l = 0
score_r = 0

# Function to create a paddle or ball object
def obj_maker(shape, xpos=0, width=1, length=1, ypos=0):
    obj = turtle.Turtle()
    obj.shape(shape)
    obj.speed(0)
    obj.color("white")
    obj.shapesize(stretch_wid=width, stretch_len=length)
    obj.penup()
    obj.goto(xpos, ypos)
    return obj

# Function to update the game state
def update_game():
    pen.clear()
    pen.write(f"Player 1: {score_l} || Player 2: {score_r}", align="center", font=("Courier", 24, "normal"))
    ball.goto(0, 0)
    ball.dx *= random.choice([-1, 1])

# Function to check if the ball touches a paddle
def touch_paddle(paddle):
    return ball.ycor() < paddle.ycor() + 50 and ball.ycor() > paddle.ycor() - 50

# Functions to move the left paddle. You can change the y value to increase or decrease the movement speed.
def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

# Functions to move the right paddle. You can change the y value to increase or decrease the movement speed.
def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)

# Create left paddle
paddle_l = obj_maker("square", -350, 5)

# Create right paddle
paddle_r = obj_maker("square", 350, 5)

# Create ball. You can change the dx and dy value to increase or decrease the ball speed.
ball = obj_maker("circle")
ball.dx = 2
ball.dy = 2

# Create the score display
pen = obj_maker(None, ypos=260)
pen.hideturtle()
pen.write(f"Player 1: {score_l} || Player 2: {score_r}", align="center", font=("Courier", 24, "normal"))

# Set up keyboard bindings
window.listen()
window.onkeypress(paddle_l_up, "w")
window.onkeypress(paddle_l_down, "s")
window.onkeypress(paddle_r_up, "Up")
window.onkeypress(paddle_r_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom border control
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.sety(290) if ball.ycor() > 290 else ball.sety(-290)
        ball.dy *= -1

    # Left and right border control
    if ball.xcor() > 390:
        score_l += 1
        update_game()
    elif ball.xcor() < -390:
        score_r += 1
        update_game()

    # Collision detection with paddles
    if (340 < ball.xcor() < 350) and touch_paddle(paddle_r):
        ball.dx *= -1
    elif (-350 < ball.xcor() < -340) and touch_paddle(paddle_l):
        ball.dx *= -1
