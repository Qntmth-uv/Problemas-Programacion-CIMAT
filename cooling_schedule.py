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



x = df.iloc[:,1].values.tolist()
y = df.iloc[:,2].values.tolist()


def aptitud_funct(secuence):
    def computingEucNormFromIndex(ind1, ind2):        
        def euclidianFunction(a: tuple, b: tuple):
            return np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
        x1 = (x[ind1], y[ind1])
        x2 = (x[ind2], y[ind2])
        return euclidianFunction(x1, x2)
    d = 0
    for i in range(0, len(secuence)-1):
        d +=computingEucNormFromIndex(secuence[i], secuence[i+1])
    return d

def permutacion(secuence):
    ranint = np.random.randint(0, len(secuence), 1)[0]
    if ranint == len(secuence) - 1:
        secuence[-1], secuence[0] = secuence[0], secuence[-1]
        return secuence
    else:
        secuence[ranint], secuence[ranint+1] = secuence[ranint+1], secuence[ranint]
        return secuence
    

def genArray(N: int):
    index_array = np.random.choice(N, N, replace=False).tolist()
    return index_array


def cooling_schedule(secuence, temperature, min_temperature, cooling_term):
    iter = 0
    while temperature > min_temperature:
        iter += 1
        secuence_aletered = permutacion(secuence[:])
        performance_alt = aptitud_funct(secuence_aletered)
        performance_original = aptitud_funct(secuence)
        print("Original: "+ str(performance_original) + ", Alterado: " + str(performance_alt))
        delta_E = performance_alt - performance_original
        if delta_E <= 0:
            secuence = secuence_aletered[:]
        else:
            dice = np.random.random()
            if dice < np.exp(-(delta_E/iter)):
                secuence = secuence_aletered[:]
            else: pass
        temperature *= cooling_term
    return secuence, aptitud_funct(secuence)


s_0 = [50, 12, 47, 45, 20, 48, 31, 35, 38, 37, 46, 0, 30, 6, 14, 40, 7, 29, 28, 2, 23, 27, 51, 10, 25, 34, 3, 43, 17, 19, 24, 36, 21, 32, 39, 33, 49, 16, 1, 41, 9, 15, 26, 13, 42, 18, 8, 4, 5, 11, 22, 44]
print(cooling_schedule(s_0, 25, 0.125, 0.95))

