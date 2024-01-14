import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1500, height=1000)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

count = 0
game_is_on = True

while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.onkeypress(player.move, "Up")

    if count % 6 == 0:
        car.create_car()

    if player.is_at_finish_line():
        player.go_to_start()
        score.level_up()
        score.update_scoreboard()
        car.car_speed()

    for obstacle in car.cars:
        if player.player.distance(obstacle) < 20:
            score.game_over()
            game_is_on = False

    car.move_car()
    screen.listen()
    screen.update()
