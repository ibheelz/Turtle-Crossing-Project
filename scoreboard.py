from turtle import Turtle

FONT = ("Courier", 16, "bold")

class Scoreboard:
    LEVEL = 1

    def __init__(self):
        self.level = self.LEVEL

        # Score turtle
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0, 440)
        self.update_scoreboard()

        # Game over turtle
        self.game_over_text = Turtle()
        self.game_over_text.hideturtle()
        self.game_over_text.penup()
        self.game_over_text.goto(0, 0)

    def update_scoreboard(self):
        self.score.clear()
        self.score.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.game_over_text.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.level += self.LEVEL
        self.update_scoreboard()
