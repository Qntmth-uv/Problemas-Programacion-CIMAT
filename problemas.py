import numpy as np

caseA1 = [2,10,3,8,5,7,9,5,3,2]
caseA2 = [771,121,281,854,885,734,486,1003,83,62]
caseA3 = [484,114,205,288,506,503,201,127,410]




##1 Subcojuntos que tienen el mismo tamaño

def aleatoryAppend(set1: list, subset1:list, remove = False):
    toadd = np.random.randint(0, len(set1), 1).tolist()[0]
    subset1.append(set1[toadd])
    if remove == True:
        set1.pop(toadd)
    return set1, subset1


##2 PESOS Y VALORES

p = [23,31,29,44,53,38,63,85,89,82]
v = [92,57,49,68,60,43,67,84,87,72]


def genAletorySecuence(N: int):
    size_sample = np.random.random_integers(0, N, size=1)
    secuence = np.random.choice(N, size_sample, replace=False)
    return secuence

s = genAletorySecuence(len(p))

def sumElemens(array, indices):
    """Funcion para calcular el peso y el valor del paquete"""
    return sum([array[ind] for ind in indices])


def permutacion(array):
    toremove = np.random.randint(0, len(array), 1).tolist()[0]
    array.pop(toremove)
    return array, toremove

def permutacion(array):
    "Intercambia dos valores de manera aleatoria"
    index_aleatory = np.random.randint(0, len(array), 2).tolist()
    array[index_aleatory[0]], array[index_aleatory[1]] = array[index_aleatory[1]], array[index_aleatory[0]]
    return array

def cooling_schulude(pesos,  valores, secuence_v, temp, min_tem, coolPar, peso_max):
    iter = 0
    while temp > min_tem: #Mientras la temperatura no decaiga
        iter += 1
        peso_actual = sumElemens(pesos, secuence_v) #Calcula el peso actual de la secuencia
        if peso_actual <= peso_max: 
            alteracion = permutacion(secuence_v[:]) 
            peso_alter = sumElemens(pesos ,alteracion)
            while peso_alter < peso_max:
                #Si sobrepasa el valor, buscamos una modificacion que si lo satifaga
                #Permutamos los indices hasta que nos de un arreglo que si satisfaga el valor 
                alteracion = permutacion(secuence_v[:])
                peso_alter = sumElemens(pesos, alteracion)
            aptitud_original = sumElemens(valores,secuence_v) # Comparacion entres aptitudes
            aptitud_alter = sumElemens(valores, alteracion) #Comparacion entres aptitudes 
            delta = aptitud_alter - aptitud_original #Mejora o no
            print(aptitud_alter, aptitud_original)
            if delta <= 0:
                secuence_v = alteracion[:] #Si mejora modificamos el arreglo
            else:
                prob = np.random.random() #Aceptamos el cambio de arreglo si satisface cierta probabilidad
                if prob > np.exp(-(delta/iter)):
                    secuence_v = alteracion[:]
            temp *= coolPar #Modificamos la temperatura
        else: #Perturbacion hasta que encuentre uno que si satisfaga
            while peso_actual > peso_max:
                secuence_v = permutacion(secuence_v[:])
                peso_actual = sumElemens(pesos, secuence_v)
                print(peso_actual)
    return secuence_v

print(p,v,s)
#print(cooling_schulude(p, v, s, 64, 2, 0.99,165))


##3 SUDOKU
def columsMaker(board):
    """Regresa las columnas de un sudoku"""
    columns = []
    for i in range(0, len(board)):
        local_column = []
        for j in range(0, len(board)):
            local_column.append(board[j][i])
        columns.append(local_column)
    return columns


def elementInrow(row, element):
    at = 0
    """Veriica si el elemento se encuentra ya en la fila"""
    for i in row:
        if element == i:
            at += 1
        else: pass
    return at

def elementInCol(col, element):
    """Veriica si el elemento se encuentra ya en la columna"""
    at = 0
    for j in col:
        if element == j:
            at += 1
        else: pass
    return at


def ThereIsOtherInNeiborhood(board, pos: tuple):
    block_x = pos[0]//3 #Calcula la posicion de en que bloque_x esta el elemento
    block_y = pos[1]//3 #Calcula la posicion de en que bloque_y esta el elemento

    element = board[pos[0]][pos[1]]
    at = 0
    for i in range(0,3):
        for j in range(0, 3):
            if board[3*block_x+i][3*block_y+j] == element:
                at += 1
            else: pass
    return at

b = [np.random.choice(np.arange(1, 10, 1), 9, replace=False).tolist() for _ in range(0, 9)]  #Generacion del tablero
print(b) 

def isASolution(board):
    """Funcion de aptitud, cuenta el numero de elementos invalidos en un sudoku"""
    choques = 0
    columns = columsMaker(board)
    for k in range(0,9):
        for l in range(0,9):
            choques += elementInrow(board[k], board[k][l])
            choques += elementInCol(columns[l], board[k][l])
            choques += ThereIsOtherInNeiborhood(board, (k,l))
    return choques                        


def permutacion_board(board):
    element_in_row_to_interchage = np.random.randint(0, 9, 1).tolist()[0]
    board[element_in_row_to_interchage] = permutacion(board[element_in_row_to_interchage])
    return board

def printasMatrix(matrix):
    for i in matrix:
        print(i)


def cooling_shudule_sudoku(board, temp, min_tem, coolingPar):
    iter = 0
    while temp > min_tem:
        iter += 1
        b_aletered = permutacion_board(board[:])
        performance_original = isASolution(board)
        performance_altered = isASolution(b_aletered)
        printasMatrix(b_aletered)
        print(performance_altered)
        print("----------------------")
        printasMatrix(board)
        print(performance_original)
        print("----------------------")
        #print(performance_original, performance_altered)
        delta = performance_altered - performance_original
        if delta <= 0:
            board = b_aletered
        else:
            prob = np.random.random()
            if prob > np.exp(-(delta/iter)):
                board = b_aletered
            else: pass
        temp *= coolingPar
    return board

#printasMatrix(cooling_shudule_sudoku(b, 64, 2, 0.98))