import turtle 

window = turtle.Screen()

window.title('Pong')
window.bgcolor('black')
window.setup(width = 800, height = 600)
window.tracer(0)

# Score 
score_1 = 0
score_2 = 0

#  Left Paddle
l_paddle = turtle.Turtle()
l_paddle.speed(0)
l_paddle.shape('square')
l_paddle.color('white')
l_paddle.shapesize(stretch_wid=5, stretch_len=1)
l_paddle.penup()
l_paddle.goto(-350, 0)


#  Right Paddle
r_paddle = turtle.Turtle()
r_paddle.speed(0)
r_paddle.shape('square')
r_paddle.color('white')
r_paddle.shapesize(stretch_wid=5, stretch_len=1)
r_paddle.penup()
r_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.xspeed = 0.25
ball.yspeed = 0.25

# Text
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player 1: 0 Player 2: 0', align = 'center', font= ('Courier', 24, 'normal'))


# Move up l_paddle
def l_paddle_up ():
    y = l_paddle.ycor()
    y += 25
    l_paddle.sety(y)

# Move down l_paddle
def l_paddle_down():
    y = l_paddle.ycor()
    y -= 25
    l_paddle.sety(y)


#  Move up r_paddle   
def r_paddle_up ():
    y = r_paddle.ycor()
    y += 25
    r_paddle.sety(y)

# # Move down r_paddle

def r_paddle_down ():
    y = r_paddle.ycor()
    y -= 25
    r_paddle.sety(y)

# keyboard binding
window.listen()
window.onkeypress(l_paddle_up,'w')
window.onkeypress(l_paddle_down,'s')
window.onkeypress(r_paddle_up,'Up')
window.onkeypress(r_paddle_down,'Down')

#  Main game loop
while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.xspeed)
    ball.sety(ball.ycor() + ball.yspeed)

    # Check borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.yspeed *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.yspeed *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.xspeed *= -1
        score_1 += 1
        pen.clear()
        pen.write('Player 1: {} Player 2: {}'.format(score_1, score_2), align = 'center', font= ('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.xspeed *= -1 
        score_2 += 1
        pen.clear()
        pen.write('Player 1: {} Player 2: {}'.format(score_1, score_2), align = 'center', font= ('Courier', 24, 'normal'))

    # collision logic right paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < r_paddle.ycor() + 40 and ball.ycor() > r_paddle.ycor() - 40):
        ball.setx(340)
        ball.xspeed *= -1
    # collision logic left paddle 
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < l_paddle.ycor() + 40 and ball.ycor() > l_paddle.ycor() - 40):
        ball.setx(-340)
        ball.xspeed *= -1