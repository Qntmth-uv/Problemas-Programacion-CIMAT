from copy import deepcopy

def sumElementsinMatrix(matrix: list[list[float]]) -> float:
    """Suma todos los elementos en la matriz.
    Input: Matriz (No necesarimente cuadrada)
    Output: Suma: floante
    -Tiempo de ejecucion: O(N)"""
    return sum([sum(row) for row in matrix])


def continuosMatrices(matrix: list[list[int]]) -> tuple:
    """Calcula el valor maximo de una submatriz de alguna función a aplicar a la submatriz. 
    Restrcciones. La matriz debe de ser cuadrada.
    Input: Una matriz M cuadrada con cualquier valor
    Output: Una submatriz de M que tiene un valor maximo de la funcion a aplciar. En este caso por defecto esta
    la funcion de sumar todos los elementos de la matriz. Pero facilmente se puede generalizar el código a cualquier otro
    maximo. Lo anterior por la modularidad del código.

    Analisis del codigo: 
    -Tiempo de ejecución. Mire que se definen cuatro funciones que crean las submatrices. El tiempo de ejecución de cada funcion
    es O(n). Por tanto en esas cuatro ejecuciones es O(4n). Posteiormente se aplica la funcion a aplicar a cada submatriz, cada una
    igual con un tiempo de ejecución O(n), sin embargo, la funcion a la que llama hace N ejecuciones. Por tanto se realizan O(n**2) 
    ejecuciones en cada aplicacion de la funcion a la submatriz. De esta forma se tienen O(4n**2). El ultimo proceso es constante
    ya que solo se checa en diccionarios que tiene tiempo de ejecución O(1).
    Por lo tanto el tiempo de ejecucion es O(n**2)

    -Complejidad espacial. Observece que por cada matriz de tamaño n tiene 4n submatrices continuas. Que se guardarán en los diccionarios
    y una variable más. Por tanto en complejidad espacial es de O(n).
    """
    def CTLtoBR(matrix: list[list[int]]) -> list[list[int]]:
        """Remueve la fila más arriba además de todos los elementos en la primera columna de la matriz a la que se le ha
        removido la fila primero"""
        matrix.pop(0)
        for i in range(0, len(matrix)):
            matrix[i].pop(0)

    def CTRtoBL(matrix: list[list[int]]) -> list[list[int]]:
        """Remueve la fila más arriba además de todos los elementos en la ultima columna de la matriz a la que se le ha
        removido primero la fila"""
        matrix.pop(0)
        for i in range(0, len(matrix)):
            matrix[i].pop()
    
    def CBLtoTR(matrix: list[list[int]]) -> list[list[int]]:
        """Remueve la fila más abajo además de todos los elemtos de la primera columna de la matriz a la que se la ha 
        removido primero la fila"""
        matrix.pop()
        for i in range(0, len(matrix)):
            matrix[i].pop(0)

    def CBRtoTL(matrix: list[list[int]]) -> list[list[int]]:
        """Remueve la fila más abajo además de todos los elemtos de la ultima columna de la matriz a la que se la ha 
        removido primero la fila"""
        matrix.pop()
        for i in range(0, len(matrix)):
            matrix[i].pop()

    ## Diccionarios donde se va a guardar el valor de aplicar cada submatriz en cada funcion. 
    CTLtoBR_Aplied_Function = dict()
    CTRtoBL_Aplied_Function = dict()
    CBLtoTR_Aplied_Function = dict()
    CBRtoTL_Aplied_Function = dict()

    #Ejecución de submatrices de izquierda superior a derecha inferior.
    copy_matrix = deepcopy(matrix)
    for _ in range(0, len(matrix)):
        CTLtoBR(copy_matrix)
        r = sumElementsinMatrix(copy_matrix) #Funcion a aplicar
        CTLtoBR_Aplied_Function[r] = deepcopy(copy_matrix) 
    
    #Ejecucion de submatrices de derecha superior a izquiera inferior
    copy_matrix = deepcopy(matrix)
    for _ in range(0, len(matrix)):
        CTRtoBL(copy_matrix)
        r = sumElementsinMatrix(copy_matrix)
        CTRtoBL_Aplied_Function[r] = deepcopy(copy_matrix)

    #Ejecucion de submatrices de izquierda inferior a derecha superior
    copy_matrix = deepcopy(matrix)
    for _ in range(0, len(matrix)):
        CBLtoTR(copy_matrix)
        r = sumElementsinMatrix(copy_matrix)
        CBLtoTR_Aplied_Function[r] = deepcopy(copy_matrix)

    #Ejecucion de submatrices de derecha inferior a izquuierda superior
    copy_matrix = deepcopy(matrix)
    for _ in range(0, len(matrix)):
        CBRtoTL(copy_matrix)
        r = sumElementsinMatrix(copy_matrix)
        CBRtoTL_Aplied_Function[r] = deepcopy(copy_matrix)    

    #Encuentra el valor máximo en cada submatriz en la función aplicada para cada funcion de creacion de submatrices.
    #Se usa un conjunto para no repetir valores, de esta forma si existe dos matrices con el mismo valor. Regresa alguno y no
    #genera un error.
    maxval = max({max(CTLtoBR_Aplied_Function.keys()), max(CTRtoBL_Aplied_Function.keys()), max(CBLtoTR_Aplied_Function.keys()), max(CBLtoTR_Aplied_Function.keys())})
    #Encuentra en que diccionario está el maximo.
    if CTLtoBR_Aplied_Function.get(maxval) != None:
        return maxval, CTLtoBR_Aplied_Function[maxval]
    elif CTRtoBL_Aplied_Function.get(maxval) != None:
        return maxval, CTRtoBL_Aplied_Function[maxval]
    elif CBLtoTR_Aplied_Function.get(maxval) != None:
        return maxval, CBLtoTR_Aplied_Function[maxval]
    else:
        return maxval, CBRtoTL_Aplied_Function[maxval]


def printAsMatrix(matrix: list[list[int]]) -> None:
    "Funcion para imprimir matrices"
    for i in matrix:
        print(i)

if __name__ == "__main__":
    matrixA = [[1,-22,30000,4],[1,2,96,4],[1,3,5,-9],[0,-1,0,-1]]
    A = continuosMatrices(matrixA)
    printAsMatrix(A)