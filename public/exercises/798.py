# === METADATA ===
# title: Filtro de Valores en Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y un valor umbral. La función debe retornar una nueva lista plana (unidimensional) que contenga únicamente los números de la matriz que sean mayores o iguales al umbral, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [10, 15, 20]
# hint: Puedes recorrer la matriz usando bucles anidados para acceder a cada elemento, almacenarlos en una lista y finalmente aplicar el método de ordenamiento .sort().

# === SOLUTION ===
def filtrar_y_ordenar_matriz(matriz, umbral):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento >= umbral:
                resultado.append(elemento)
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert filtrar_y_ordenar_matriz([[1, 5], [10, 2]], 5) == [5, 10], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_matriz([[8, 2], [3, 9], [1, 5]], 4) == [5, 8, 9], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_matriz([[0, 0], [0, 0]], 1) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")