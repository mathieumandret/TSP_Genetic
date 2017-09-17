from utils import init_map
from networkx import *
from numpy import *
import matplotlib.pyplot as plt

arr = array([[0,1,2,6],
             [0,0,4,7],
             [0,0,0,8],
             [0,0,0,0]])
G = networkx.from_numpy_matrix(arr)
G2 =  networkx.Graph([(1,1)])
A = networkx.adjacency_matrix(G)
print(A)
