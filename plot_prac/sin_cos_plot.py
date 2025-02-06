import pylab as p
from numpy import *

p.title('Sine and Cosine')
p.xlabel('x')
p.ylabel('f(x)')

min_datapoint = -pi
max_datapoint = pi
intervals = (max_datapoint - min_datapoint) / 500

x = arange(min_datapoint, max_datapoint, intervals)
y = sin(x)
z = cos(x)

p.plot(x, y, 'r')
p.plot(x, z, 'g')

p.savefig('trig_plot.png', dpi=300)
p.show()
