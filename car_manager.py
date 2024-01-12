import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        self.car = Turtle()
        self.car.penup()
        self.car.shapesize(2, 4)
        self.car.shape("square")
        self.color = random.choice(COLORS)
        self.car.color(self.color)
        self.car.setheading(180)
        self.car.setposition(790, random.randint(-400, 400))
        self.cars.append(self.car)

    def move_car(self):
        for car in self.cars:
            car.fd(self.speed)

    def car_speed(self):
        self.speed += MOVE_INCREMENT

    def detect_collision(self, player):
        for car in self.cars:
            if player.player.distance(car) < 35:
                return True
        return False