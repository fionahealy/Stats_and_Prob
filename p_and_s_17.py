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

event_split = events.split()
print(event_split)

for event in event_split:
	event_value = balls[event]







