import random
from matplotlib import pyplot
import numpy
from scipy import optimize
from astropy.modeling import models, fitting

sums = []
die_rolls = 2
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

pyplot.plot(numpy.arange(1,plot_range),counts)
pyplot.grid()
pyplot.show()

g_init = models.Gaussian1D(amplitude=1., mean=0, stddev=1.)
fit_g = fitting.LevMarLSQFitter()
g = fit_g(g_init, numpy.arange(1,plot_range), counts)