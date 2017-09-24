from population import Population

nombre_villes = 100
effectif_initial = 5
mutation = 10
generations = 30

p = Population(effectif_initial, nombre_villes)
print(p)
for i in range(generations):
    p.evolve(effectif_initial, mutation)
    print(p)
