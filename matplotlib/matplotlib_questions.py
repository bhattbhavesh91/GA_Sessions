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