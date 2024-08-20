from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    # segments[0].left(90)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.add_length()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collistion with tail
    for seg in snake.segments[1:]:
        # if seg == snake.head:
        #     pass
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
