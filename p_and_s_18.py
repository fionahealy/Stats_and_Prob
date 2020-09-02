
import numpy

die_roll = input("Roll the die? (Y/N) ")

die_sample_space = 6

probs = []

while die_roll == "Y":
	bet = input("Place your bet: (1 - 6, comma separated) ")
	bet_list = bet.split(",")
	probs.append(len(bet_list)/die_sample_space)
	roll_again = input("Roll again? (Y/N) ")
	die_roll = roll_again

total_prob = numpy.prod(probs)
print(total_prob)

