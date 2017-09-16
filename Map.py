import networkx as nx
from itertools import permutations

#Soit un graphe avec 3 sommets A,B,C
#et 3 arêtes: A -> B (-2)
#             B -> C (-3)
#             C -> A (-1)

#Instanciation de la carte
Map = nx.Graph();
#Ajout des villes (noeuds)
for nom in ['A','B','C']:
    Map.add_node(nom)
    

#Ajout des chemins
Map.add_edge('A','B')
Map.add_edge('B','C')
Map.add_edge('C','A')
#Ajout des poids des chemins
Map['A']['B']['poids'] = -2
Map['B']['C']['poids'] = -3
Map['C']['A']['poids'] = -1

#Verification
print("Nombre de villes", Map.number_of_nodes())
print("Liste des villes", Map.nodes())
print("Liste des chemins", Map.edges())
print("Poids de A->B =", Map['A']['B']['poids'])

def get_path_weight(path):
    """
    Etant donne une liste de sommets
    retourne le poids du chemin parcourant
    tous ces sommets dans l'ordre
    """
    #En partant de la fin
    premiere_ville = str(path.pop())
    deuxieme_ville = str(path.pop())
    poids_v1_v2 = Map[premiere_ville, deuxieme_ville]['poids']
    return poids_v1_v2;


def createMap():
    carte = {
            'A': {'B': 2, 'C': 3},
            'B': {'A': 5, 'C': 8},
            'C': {'A': 1, 'B': 2},
            }

