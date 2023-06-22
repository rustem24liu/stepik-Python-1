from pylab import *

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
x = arange(0, 30, 5)
y = x*2
axes.plot(x, y, 'g')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('home work')
show()