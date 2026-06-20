# === METADATA ===
# title: Filtro de Matrices con Umbral
# description: Dada una matriz (lista de listas) de números enteros y un valor umbral, devuelve una nueva lista unidimensional que contenga únicamente los elementos de la matriz que sean estrictamente mayores al umbral, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [5, 6, 8, 9] (dada una matriz con valores hasta 9 y umbral 4)
# hint: Puedes recorrer la matriz usando bucles anidados para acceder a cada elemento, añadir los válidos a una lista simple y finalmente usar el método sort().

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
    assert filtrar_y_ordenar_matriz([[9, 5], [1, 8], [6, 2]], 4) == [5, 6, 8, 9], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_matriz([[0, 0], [0, 0]], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")