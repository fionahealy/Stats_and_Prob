import random
from matplotlib import pyplot
import numpy
from scipy import optimize
from astropy.modeling import models, fitting

sums = []
die_rolls = 100
plot_range = die_rolls*6+1

for i in range(0,10000):

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

g_init = models.Gaussian1D(amplitude=100., mean=350, stddev=50.)
fit_g = fitting.LevMarLSQFitter()
g = fit_g(g_init, numpy.arange(1,plot_range), counts)

pyplot.plot(numpy.arange(1,plot_range),g(numpy.arange(1,plot_range)))
pyplot.show()
