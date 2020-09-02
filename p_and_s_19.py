import random
from matplotlib import pyplot
import numpy
from collections import Counter

sums = []
die_rolls = 10
plot_range = die_rolls*6+1

for i in range(0,100000):

	rolls = []

	for roll in range(1,die_rolls+1):

		die_roll = random.randint(1,6)
		rolls.append(die_roll)

	sum_dice = numpy.sum(rolls)

	sums.append(sum_dice)

# pyplot.plot(sums)
# pyplot.show()

counts = []
for i in range(1,plot_range):
	count = sums.count(i)
	counts.append(count)

print(counts)

pyplot.plot(numpy.arange(1,plot_range),counts)
pyplot.grid()
pyplot.show()