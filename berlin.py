import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Close input file

file1 = pd.read_csv("berlin52.csv", index_col=False, header=None)

arr = np.array(file1)
nodo, x, y = [], [], []

for el in arr:
    nodo.append(float(el[0].split(" ")[0]))
    x.append(float(el[0].split(" ")[2]))
    y.append(float(el[0].split(" ")[1]))

df = pd.DataFrame({"nodo": nodo, "x": x, "y": y})

#xplt.scatter(x,y)
#plt.show()

def euclidianFunction(a: tuple, b: tuple):
    return np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


x = df.iloc[:,1].values.tolist()
y = df.iloc[:,2].values.tolist()


aleatory_index = np.random.randint(0, len(x), 1).tolist()[0]

def computingMinimum(x,y, index_b = 0):
    """Calcula la distancia minima entre un conjunto de datos
    
    Entrada
    -----------
    x - Conjunto de absisas de puntos
    y - Conjunto de ordenadas de puntos
    index_b - Indice donde empezará a buscar el valor más chico

    Regresa
    -----------
    float - Distancia mínima para recorrer el camino.
    """
    index = index_b
    abslutes_distances = []
    while len(x)!= 1 and len(y) != 1:
        starting_point = (x[index], y[index])
        local_distancs = []
        for i in range(0, len(x)):
            if i != index:
                d = euclidianFunction(starting_point, (x[i], y[i]))
                local_distancs.append(d)
            else: pass
        abslutes_distances.append(min(local_distancs))
        index = local_distancs.index(abslutes_distances[-1])
        x.pop(index)
        y.pop(index)
    return sum(abslutes_distances)

def bestPointToStart(x,y) -> tuple:
    """Calcula la distancia minima entre todos los puntos de inicio
    
    Entrada
    -----------
    x - Conjunto de absisas de puntos
    y - Conjunto de ordenadas de puntos
    index_b - Indice donde empezará a buscar el valor más chico

    Regresa
    -----------
    float - Distancia mínima para recorrer el camino."""
    minimumset = []
    for i in range(0, len(x)):
        minimumset.append(computingMinimum(x[:], y[:], i))
    minimum_distance = min(minimumset)
    index_minimum = minimumset.index(minimum_distance)
    return minimum_distance, index_minimum 

print(bestPointToStart(x,y))
