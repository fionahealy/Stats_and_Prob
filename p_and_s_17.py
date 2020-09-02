import math
import numpy

def parenthesis_finder(str):
	inner_str = str[str.find("(")+1:str.rfind(")")]
	return inner_str

events = input("Enter event:")

balls = {
	"blue":5.0,
	"red":6.0,
	"white":4.0
}

balls_list = list(balls.values())

total_balls = sum(balls_list)

inside_parenthesis = parenthesis_finder(events)
print(inside_parenthesis)

# event_split = events.split()
# print(event_split)

# for event in event_split:
# 	event_value = balls[event]




#examples: red, red or white, red and not white, not (blue or white),
#(not blue) or white, red and (not white or blue), red or not white,
#(red and not white) or blue






