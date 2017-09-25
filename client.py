from population import Population

nombre_villes = 100
effectif_initial = 10
mutation = 10
gens = 2

p = Population(effectif_initial, nombre_villes)
print(p)
for x in range(gens):
    print(p)
    p.evolve(mutation)
print(p)
