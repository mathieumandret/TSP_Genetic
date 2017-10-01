#coding: utf-8

from Population import Population
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

p = Population(20,250)
p.eval()
best = p.meilleurChemin

x, y = best.toPlot()

fig1 = plt.figure()
plt.scatter(x,y)
graph, = plt.plot(x,y)


def animer(i):
    p.evoluer(10)
    best = p.meilleurChemin
    nx, ny = best.toPlot()
    graph.set_data(nx,ny)

ani = FuncAnimation(fig1, animer, interval=20)

plt.show()





