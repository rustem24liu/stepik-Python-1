from pylab import *

x = linspace(0, 5, 9)
y = x**0.5

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1 , 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5 , 0.4, 0.3])

axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('graph number 1')

axes2.plot(x, y, 'g')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_title('graph number 2')

show()

