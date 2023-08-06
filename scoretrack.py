from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 280)
        self.color("green")
        self.update()
        self.hideturtle()

# Making a turtle write score
    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

# Refresh the score board
    def refresh(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../../../Office 2010/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

# Adding to user's score
    def increase(self):
        self.score += 1
        self.update()
