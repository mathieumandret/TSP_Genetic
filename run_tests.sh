#!/bin/bash

if [ -d $HOME/Python/TSP_Genetic ]; then
    folder=$HOME/Python/TSP_Genetic
elif [ -d $HOME/workspace/Python/TSP_Genetic ]; then
    folder=$HOME/workspace/Python/TSP_Genetic  
fi

export PYTHONPATH=$folder:$PYTHONPATH
    
echo "Test de la classe ville"
python3 tests/test_ville.py 
echo "Test de la classe chemin"
python3 tests/test_chemin.py
echo "Test de la classe population"
python3 tests/test_population.py
