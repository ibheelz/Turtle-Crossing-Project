import random
from scoreboard import Scoreboard
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shapesize(2, 4)
        new_car.shape("square")
        color = random.choice(COLORS)
        new_car.color(color)
        new_car.setheading(180)
        new_car.setposition(790, random.randint(-400, 400))
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.fd(self.speed)

    def car_speed(self):
        self.speed += MOVE_INCREMENT
