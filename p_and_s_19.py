import random
import numpy
from matplotlib import pyplot
from scipy.optimize import curve_fit
from scipy.stats import norm
import os
#--------init-----------------------------------

sums = []
die_rolls = 200
reps = 100000

plot_range = die_rolls*6+1
x_range = numpy.arange(1,plot_range)

#--------die-rolls------------------------------

for i in range(0,reps):

	rolls = []

	for roll in range(1,die_rolls+1):

		die_roll = random.randint(1,6)
		rolls.append(die_roll)

	sum_dice = numpy.sum(rolls)

	sums.append(sum_dice)

#--------frequency-distribution-of-sums-----------

counts = []
for i in range(1,plot_range):
	count = sums.count(i)
	counts.append(count)

#--------gaussian-fit-----------------------------

mean = numpy.mean(sums)
sigma = numpy.std(sums)

def gaussian_func(mean,sigma,x):
	gauss = (reps/(sigma*numpy.sqrt(2*numpy.pi)))\
			*numpy.exp(-((x-mean)**2/(2*sigma**2)))
	return gauss

#print(gaussian_func(1,1,1,1))
popt, pcov = curve_fit(gaussian_func, x_range, counts,p0=[mean,sigma])

mean_fit = popt[1]
std_fit = popt[0]
pcov_string = "["+"{:.2e}".format(pcov[0,0])+", "+"{:.2e}".format(pcov[0,1])+"\n"\
				+"{:.2e}".format(pcov[1,0])+", "+"{:.2e}".format(pcov[1,1])+"]"
#--------plot-data-------------------------------
props = dict(boxstyle='square', facecolor='#B9D6F2', alpha=0.5)
pyplot.plot(x_range,counts,color="#061A40",linewidth=3,alpha=1)
pyplot.xticks(font="Menlo")
pyplot.yticks(font="Menlo")
pyplot.xlabel("Sum of dice rolls",font="Menlo")
pyplot.ylabel("Frequency of sum occurance",font="Menlo")
pyplot.grid(color='#D7D9D7', linestyle='--', linewidth=0.3)
pyplot.text(0.05, max(counts)-max(counts)/100,pcov_string, fontsize=11,font="Menlo",verticalalignment='top',bbox=props)
#--------plot-gaussian-------------------------------

pyplot.hist(sums,bins=numpy.arange(0,plot_range)+0.5,color="#0075A2")

p = gaussian_func(mean_fit,std_fit,x_range)
pyplot.plot(x_range, p, 'k', linewidth=1,linestyle='--',alpha=1,color="#BCE784")
os.system('say "meow"')

pyplot.show()
