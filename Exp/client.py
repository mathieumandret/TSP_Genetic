from city import City
from chemin import Chemin
from population import Population

p = Population(10,5)
print(p)
print(p.getFittest())
p.orderByFitness()
print(p)
    
