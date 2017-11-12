# coding: utf-8
from math import cos, sin
from csv import writer

coords = []
x = []
y = []
r = 10

for i in range(0, 360, 10):
    rad = 0.01745329252 * i
    x.append(r * cos(rad))
    y.append(r * sin(rad))

for i in range(len(x)):
    coords.append((x[i], y[i]))


with open('cercle.csv', 'w') as f:
    w = writer(f)
    w.writerows(coords)
