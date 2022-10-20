from pylab import *

x = linspace(0, 5, 10)
y = x ** 2


##pylab -> global plot -> not good
figure()
plot(x,y ,'r')
xlabel('x')
ylabel('y')
title('title')


#subplot(1,2,1)
#plot(x, y, 'r--')
#subplot(1,2,2)
#plot(y, x, 'g*-')

#show()


##OOP method of plotting, therefore you can create multiple figures at once
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #left, bottom, width, height (range 0 to 1)
axes.plot(x,y,'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title_oop')


#able to place the axes where ever you need them
fig_1 = plt.figure()

axes1 = fig_1.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig_1.add_axes([0.2, 0.5, 0.3, 0.5]) # inset axes

# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title_outer')

# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title');

show()
