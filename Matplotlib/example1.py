from pylab import *

x = linspace(0, 5, 9)
y = x**2
print(x)
print(y)

figure()
plot(x, y, 'g')
xlabel('x')
ylabel('y')
title('just')
show()