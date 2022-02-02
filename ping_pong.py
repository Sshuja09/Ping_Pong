import turtle
import random

window = turtle.Screen()
window.title ("PONG GAME!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score_l = 0
score_r = 0

def obj_maker(shape, xpos = 0, width=1, lenght=1, ypos=0):
    obj = turtle.Turtle()
    obj.shape(shape)
    obj.speed(0)
    obj.color("white")
    obj.shapesize(stretch_wid=width, stretch_len=lenght)
    obj.penup()
    obj.goto(xpos, ypos)
    return obj

def update_game():
    pen.clear()
    pen.write(f"Player 1: {score_l} || Player 2: {score_r}", align="center", font=("Courier", 24, "normal"))
    ball.goto(0, 0)
    ball.dx *= random.choice([-1, 1])

def touch_paddle(paddle):
    return ball.ycor() < paddle.ycor() + 50 and ball.ycor() > paddle.ycor() - 50

def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)


#Left Paddle
paddle_l = obj_maker("square", -350, 5)

# Right Paddle
paddle_r = obj_maker("square", 350, 5)

# Ball
ball = obj_maker("circle")
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = obj_maker(None, ypos=260)
pen.hideturtle()
pen.write(f"Player 1: {score_l} || Player 2: {score_r}", align="center", font=("Courier", 24, "normal"))

window.listen()

window.onkeypress(paddle_l_up, "w")
window.onkeypress(paddle_l_down, "s")

window.onkeypress(paddle_r_down, "Down")
window.onkeypress(paddle_r_up, "Up")

while True:

    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom boarder control
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    # Left and right boarder control
    if ball.xcor() > 390:
        score_l += 1
        update_game()
    elif ball.xcor() < -390:
        score_r += 1
        update_game()

    # Collision detection
    if (ball.xcor() > 340 and ball.xcor() < 350) and touch_paddle(paddle_r):
       ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and touch_paddle(paddle_l):
        ball.dx *= - 1
