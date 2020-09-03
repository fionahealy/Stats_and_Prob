import random
import numpy
from matplotlib import pyplot
from scipy.stats import norm

sums = []
die_rolls = 3
plot_range = die_rolls*6+1

for i in range(0,1000):

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

mean,std=norm.fit(counts)
print(mean)
y = norm.pdf(numpy.arange(1,plot_range), mean, std)

pyplot.plot(numpy.arange(1,plot_range),counts)
pyplot.grid()
pyplot.plot(numpy.arange(1,plot_range),y)
pyplot.show()
