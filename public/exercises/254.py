# === METADATA ===
# title: Filtro de Valores en Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y un valor umbral. La función debe retornar una nueva lista plana (unidimensional) que contenga únicamente los números de la matriz que sean estrictamente mayores al umbral, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [5, 7, 8, 9] para una matriz [[1, 5], [7, 2], [9, 8]] y umbral 4
# hint: Puedes recorrer la matriz usando un bucle anidado o list comprehension, luego usa el método .sort() o la función sorted() para ordenar el resultado.

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
    assert filtrar_y_ordenar_matriz([[1, 5], [7, 2], [9, 8]], 4) == [5, 7, 8, 9], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_matriz([[10, 20], [5, 30]], 25) == [30], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_matriz([[1, 2], [3, 4]], 10) == [], "Error: el caso base (sin elementos mayores) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")