# coding: utf-8

import csv
import matplotlib.pyplot as plt

# gen = []
# fit = []
# i = 1
# with open('test.csv', 'r') as data:
#     r = csv.reader(data)
#     for ligne in r:
#         gen.append(i)
#         fit.append(ligne[0])
#         i += 1
# print(gen)

x = []
for i in range(10, 130, 10):
    x.append(i)
y = [4.19, 6.21, 9.3, 12.04, 15.58, 22.32,
     24.54, 29.15, 35.92, 41.24, 48.03, 55.54]


fig = plt.figure()
plt.xlabel("Nombre de villes")
plt.ylabel("Temps d'execution (s)")
plt.plot(x, y)
fig.savefig('Dossier/cities.png')
plt.show()
plt.show()
