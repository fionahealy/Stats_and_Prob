import random
import numpy
from matplotlib import pyplot

sums = []
die_rolls = 3

plot_range = die_rolls*6+1
x_range = numpy.arange(1,plot_range)

for i in range(0,1000):

	rolls = []

	for roll in range(1,die_rolls+1):

		die_roll = random.randint(1,6)
		rolls.append(die_roll)

	sum_dice = numpy.sum(rolls)

	sums.append(sum_dice)


counts = []
for i in range(1,plot_range):
	count = sums.count(i)
	counts.append(count)


pyplot.plot(x_range,counts)
pyplot.show()
