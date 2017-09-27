from population import Population

nombre_villes = 250
effectif_initial = 10
mutation = 10

p = Population(effectif_initial, nombre_villes)
p.evolve(mutation)
print(p)
