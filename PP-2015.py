import math

def couting_letter_a(lista_dada):
    """""Algoritmo que cuenta cuantas veces aparece un a de manera aislada en un str"""
    try:
        dim = len(lista_dada)
        contador = 0
        for i in range(0, dim-1, 1):
            if lista_dada[i] == "a":
                if (lista_dada[i-1]=="a" or lista_dada[i+1]=="a"):
                    pass
                else: 
                    contador += 1
        return contador
    except IndexError as f:
        return print("La lista tuvo un error al tratar la dimensión")    
    

def sum_diagonals_matrix(matriz: list) -> list:
    """""Calcula un array con la suma de los elementos de la diagonal de cualquier fila"""
    suma_elementos_diag = []
    contador = 1
    while matriz != []:
            suma_actual_diag = 0
            for i in range(0, contador, 1):
                if contador == len(matriz):
                    pass
                elif contador < len(matriz):
                    contador += 1
                suma_actual_diag += matriz[i][-1]
                matriz[i].pop(-1)
            if matriz[0] == []:
                matriz.pop(0)
                contador += -1
            suma_elementos_diag.append(suma_actual_diag)
    return suma_elementos_diag


def Euclidian_distance(x: float, y: float, x_0: float, y_0: float) -> float:
    """"Calcula la distancia entre dos puntos dados, usando la norma euclidiana"""""
    distance = math.sqrt((x_0-x)**2+(y_0-y)**2)
    return distance


def custom_distance(X_points, Y_points):
    """"Calcula la distancia entre dos puntos de una manera particular, primero calcula entre todas las distancias
    de los puntos de Y y variando los de X, para sacar la distancia minima la iteración, posteriormente de haber
    pasado todos los puntos de X, se saca la distancia maxima de todas las distancias minimas. La función devuelve 
    dicho valor máximo
    
    -Requiere que los inputs ya esten se encuentren los puntos en parejas"""
    distance = []
    distance_min = []
    for i in range(0, len(X_points), 1):
        for j in range(0, len(Y_points), 1):
            distance_eu = Euclidian_distance(X_points[i][0], X_points[i][1], Y_points[j][0], Y_points[j][1])
            distance.append(distance_eu)
        distance_min.append(min(distance))
    return max(distance_min)            


def Haussdorf_distance(X_points, Y_points):
    """"Usando las funciones anteriores, se saca el valor maximo de usar la custom_distance 
    variando los valores de los puntos."""
    if len(X_points) != len(Y_points):
        return "La dimension de los puntos no coincide"
    else:
        d_1 = custom_distance(X_points, Y_points)
        d_2 = custom_distance(Y_points, X_points)
    return max([d_1,d_2])


def is_int_a_2pow(numero: int) -> bool:
    """"Calcula si un entero dado es un numero que es una potencia de 2. Si es una potencia regreas
    True, mientras que si no lo es regresa falso."""
    if type(numero) != int:
        return "El numero ingresado no es un numero entero"
    else:
        while numero % 2 ==0:
            numero = numero/2
            if numero == 1:
                return True
        if numero % 2 == 1:
            return False
        

def sistem_2x2_solution_finder(a: float, b: float, c: float, d:float, e:float, f:float):
    """"Funcion que determina si un sistema 2x2 tiene una solución o una infinidad, esto
    a traves del uso del determinante y el valor explicito de las soluciones si existe.
    Debido a como esta escrito el programa, el tiempo de ejecución de esta solución es constante
    y por lo tanto es optima. Sin embargo, no es escalable-"""
    determinante = a*e-b*d
    if determinante == 0:
        return (0,0,"SolutionType: 2")
    else:
        x = 1/determinante * (c*d-b*f)
        y = 1/determinante * (a*f-e*c)
        return (x,y,"SolutionType: 1")
    

def countDiffWays(data: list, s: int):
    """""Cuenta las distintas manera de poder sumar el numero s dada una lista que contienen numero enteros."""
    dimension = len(data)
    data_set = set(data)
    dimension_set = len(data_set)
    if dimension != dimension_set:
        return "Hay valores que se repiten"
    else:
        sum_values = []
        #data.sort()
        count = 0 
        if s in data:
            sum_values.append([[s,0]])
            data.remove(s)
            count += 1
        if 0 in data:
            sum_values.append([[0,s]])
            count += 1
            data.remove(0)
        for i in data:
            if i > s:
                data.remove(i)
        counting = iter_sum_values(data, s, 0, sum_values)
        return counting/2+count, sum_values
             
    

def iter_sum_values(lista: list, s, count, sum_values) -> int:
    """""Función iterable que se usa para poder contar el como se pueden expresar los elementos
    de la suma, donde d,i son elementos en el array. 
    
    -Logra contar las maneras que se puede sumar s en los elementos de la lista, más no logra contar 
    el reexpresar los elemntos de la suma en terminos de los elementos de la misma lista."""
    for i in lista:
        d = s-i
        if i == d:
            pass
        elif d < 0:
            pass
        elif d in lista:
            count += 1
            lista.remove(i)
            sum_values.append([i, d])
            iter_sum_values(lista, d, count, sum_values)
        else:
            pass
    return count



#-------------------- TEST DE LOS ALGORITMOS ---------------#
#print("***")
#print(countDiffWays([1,2,5,4,9,3,6,7], 7))
#print("***")


#ejemplo = "adaafagrra0"
#matrix_example = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#print(sum_diagonals_matrix(matrix_example))


#Z = [[1,2],[1,8],[0,0],[7,3]]
#W = [[0,1],[0,0],[12,3],[1,9]]

#X=[[1,1],[0,0]]
#Y=[[1,-1],[0,0]]

#print(Haussdorf_distance(X,Y))
#print(is_int_a_2pow(1084))
#print(sistem_2x2_solution_finder(2,1,5,1,1,3))
#print(len(matrix_example[0][1]))
#print(couting_letter_a(ejemplo))