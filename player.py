from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -480)
FINISH_LINE_Y = 480


class Player:
    MOVE_DISTANCE = 10

    def __init__(self) -> None:
        self.scoreboard = Scoreboard()
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.shapesize(2, 2)
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)
    
    def move(self):
        self.player.fd(self.MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.player.ycor() > FINISH_LINE_Y:
            self.scoreboard.level_up()
            return True
        return False
    
    def go_to_start(self):
        self.player.goto(STARTING_POSITION)