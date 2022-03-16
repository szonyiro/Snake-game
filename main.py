import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
speed = time.sleep(0.10)
# segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    speed = 0.1
    """while loop for moving the snake by one square forward until the 
    game is over by hitting the wall or tail."""
    screen.update()
    time.sleep(speed)
    snake.move()

    if snake.head.distance(food) < 25:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    if snake.head.xcor() < -295 or snake.head.xcor() > 295 \
            or snake.head.ycor() < -295 or snake.head.ycor() > 295:
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

if not game_is_on:
    scoreboard.game_over()

# snake.move()

screen.exitonclick()
