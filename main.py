#coding: utf-8

from Population import Population

p = Population(10, 10)

for i in range(100):
    p.evoluer(10)

print(p)
