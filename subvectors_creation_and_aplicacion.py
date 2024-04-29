def sumvectorElements(vector: list[float]) -> float:
    """Calcula la suma de todos los elementos en el vector"""
    return sum(vector)

def Continuos_vector_machine(vector: list[float]) -> list[list[float]]:
    """Calcula todos los subvectores del vector dado de manera continua.
    Input: Vector (list)
    Output: Subvectors (list[list[float]])

    Tiempo de ejecucion: O(n**2)
    Complejidad espacial: O((1/2)(n)(n+1)) -> O(n**2)
    """
    vectors_list: list[list[float]] = []
    for i in range(0, len(vector)+1):
        for k in range(i, len(vector)):
            vectors_list.append(vector[i:k+1])
    return vectors_list

def applicationCS(vector: list[float]) -> tuple:
    """Aplica la función que se desea a los subvectores continuos al vector dado, y regresa el vector que maximiza el resultado.
    
    Input: Vector (list)
    Output: (MaximoValor, ElemntMax) (tupla(float, list))

    Tiempo de ejecucion: Mismo que Continuos_vector_machine.
    Complejidad espacial: O(2n**2) -> O(n**2)
    """
    vectors = Continuos_vector_machine(vector)
    vectors_sum = [sumvectorElements(subvector) for subvector in vectors]
    try:
        max_val = max(vectors_sum)
    except ValueError: return None
    else:
        return vectors[vectors_sum.index(max_val)]

if __name__ == "__main__":
    v1 = [0,0]
    print(applicationCS(v1))