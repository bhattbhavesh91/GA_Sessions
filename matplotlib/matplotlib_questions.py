import matplotlib.pyplot as plt
import numpy

def plot1 ():
	x = numpy.arange(0,20,0.1)
	y = numpy.square(x)
	plt.plot(x,y)
	return plt.show()

def plot2 ():
	x = numpy.arange(0,20,0.1)
	y1 = numpy.sin(x)
	y2 = numpy.cos(x)
	plt.plot(x,y1)
	plt.plot(x,y2)
	return plt.show()

def plot3 ():
	x = numpy.arange(0,20,0.1)
	y1 = numpy.sin(x)
	y2 = numpy.cos(x)
	plt.plot(x,y1, label='Sin of X')
	plt.plot(x,y2, label='Cosine of X')
	plt.xlabel('Time ')
	plt.ylabel('Amplitude')
	plt.legend()
	return plt.show()

def plot4 ():
	x = numpy.arange(0,20,0.1)
	y1 = numpy.cos(x)
	y2 = numpy.exp(-x/10)* numpy.cos(x)
	plt.plot(x,y1, label='Oscillation 1', linewidth = 7, color = 'b', linestyle = ':')
	plt.plot(x,y2, label='Oscillation 2', linewidth = 5, color = 'y', linestyle = '-.')
	plt.xlabel('$x$ axis', size=24)
	plt.ylabel('$y$ axis', size=24)
	plt.legend(prop={'size': 24})
	return plt.show()

def plot5 ():
	x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
	popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
	x_pos = [i for i, _ in enumerate(x)]
	plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
	plt.xlabel("Languages")
	plt.ylabel("Popularity")
	plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
	plt.xticks(x_pos, x)
	return plt.show()

def plot6():
	n_groups = 5
	men_means = (22, 30, 33, 30, 26)
	women_means = (25, 32, 30, 35, 29)

	# create plot
	fig, ax = plt.subplots()
	index = numpy.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8

	rects1 = plt.bar(index, men_means, bar_width, alpha=opacity, color='g', label='Men')
	rects2 = plt.bar(index + bar_width, women_means, bar_width, alpha=opacity, color='r', label='Women')

	plt.xlabel('Person')
	plt.ylabel('Scores')
	plt.title('Scores by person')
	plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
	plt.legend()
	return plt.show()

