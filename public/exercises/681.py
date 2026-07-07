# === METADATA ===
# title: Filtro de Valores en Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y un valor umbral. La función debe retornar una nueva lista plana (unidimensional) que contenga únicamente los números de la matriz que sean estrictamente mayores al umbral, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [5, 7, 8, 9] (para matriz [[1, 5], [9, 2], [7, 8]] y umbral 4)
# hint: Puedes usar un bucle anidado para recorrer cada fila y columna, y el método .sort() o la función sorted() para ordenar el resultado final.

# === SOLUTION ===
def filtrar_y_ordenar_matriz(matriz, umbral):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > umbral:
                resultado.append(elemento)
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert filtrar_y_ordenar_matriz([[1, 5], [9, 2], [7, 8]], 4) == [5, 7, 8, 9], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_matriz([[10, 20], [5, 3]], 15) == [20], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_matriz([[1, 2], [3, 4]], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")