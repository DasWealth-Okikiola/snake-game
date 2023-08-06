from turtle import Screen
from snake import Snake
from food import Food
from scoretrack import Score
import time

# Setting my screen
view = Screen()
view.setup(width=600, height=600)
view.bgcolor("black")
view.title("My Snake Game")
view.tracer(0)

# Importing Game's characters from their classes.
snake = Snake()
food = Food()
score = Score()

# setting the snake controls by using the listen feature and onkey.
view.listen()
view.onkey(snake.up, "Up")
view.onkey(snake.up, "u")
view.onkey(snake.down, "Down")
view.onkey(snake.down, "d")
view.onkey(snake.left, "Left")
view.onkey(snake.left, "l")
view.onkey(snake.right, "Right")
view.onkey(snake.right, "r")

# Setting the snake to always move forward as long as the game is on
# setting the view to be perfect

on = True
while on:
    view.update()
    time.sleep(0.25)
    snake.move_snakes()

    # detect collision with food by using the distance method.
    if snake.head.distance(food) < 14:
        # Bring another food
        food.refresh()
        # make snake longer
        snake.extend()
        # Add to scoreboard
        score.increase()

    # detects collision with wall.
    # By checking the distance of the head to the wall to be close.(collision)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.refresh()
        snake.reset()

    # detect collision with tail.
    # By looping through each segment(line) of snake and checking the distance of the head to it.
    # Starting the loop from the second line, using slicing

    for line in snake.full_line[1:]:

        if snake.head.distance(line) < 10:
            score.refresh()
            snake.reset()

view.exitonclick()
