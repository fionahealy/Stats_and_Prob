import math
import numpy

events = input("Enter event:")

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

event_split = events.split()

for event in event_split:
	event_value = balls[event]
	print(event_value)

# event_split = event.split()
# print(event_split)
# nots = "not" in event_split
# ors = "or" in event_split


p_red = red_balls/total_balls




