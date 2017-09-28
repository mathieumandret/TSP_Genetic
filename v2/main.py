#coding: utf-8

from Population import Population

p = Population(7, 10)
p.evoluer(10)
p.evoluer(1)
print(type(p))
print(type(p.individus[0][0]))
