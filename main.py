#coding: utf-8

from Population import Population

p = Population(5, 10)
print(p)
for i in range(1000):
    p.evoluer(20)
print(p)
