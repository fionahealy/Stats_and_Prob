import math
import numpy

event = input("Enter event:")

balls = {
	"blue":5.0,
	"red":6.0,
	"white":4.0
}

balls_list = list(balls.values())

total_balls = sum(balls_list)

red_balls = balls["red"]
blue_balls = balls["blue"]
white_balls = balls["white"]

event_value = balls[event]
print(event_value)






