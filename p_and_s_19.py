import random
from matplotlib import pyplot

sums = []

for i in range(0,100):

	die_roll_1 = random.randint(1,6)
	die_roll_2 = random.randint(1,6)

	sum_dice = die_roll_2+die_roll_1

	sums.append(sum_dice)

pyplot.plot(sums)
pyplot.show()

