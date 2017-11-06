#coding: utf-8

import numpy
from math import factorial
from matplotlib import pyplot as plt

def square(x):
    return x*x
def times_to(x):
    return 10*x

x = numpy.arange(7)
y_square = list(map(square, x))
y_fact = list(map(factorial, x))
y_two = list(map(times_to, x))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('n')
ax.set_ylabel('f(n)')
plt.plot(x,y_square, label="n^2")
plt.plot(x,y_fact, label="n!")
plt.plot(x,y_two, label="nx10")
plt.legend()
plt.savefig("complexite.png")
