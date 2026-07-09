# === METADATA ===
# title: Filtro de Valores en Matriz
# description: Dada una matriz (lista de listas) de números enteros y un valor umbral, devuelve una lista plana con todos los elementos de la matriz que sean estrictamente mayores al umbral, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [5, 6, 7, 8, 9] (para una matriz con valores del 1 al 9 y umbral 4)
# hint: Puedes usar dos bucles anidados para recorrer la matriz o una comprensión de listas, y posteriormente aplicar el método sort().

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
    assert filtrar_y_ordenar_matriz([[1, 2], [3, 4]], 2) == [3, 4], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_matriz([[10, 5], [2, 8]], 6) == [8, 10], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_matriz([[1, 1], [1, 1]], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")