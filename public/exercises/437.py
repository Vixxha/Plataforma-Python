# === METADATA ===
# title: Filtrado de Valores en Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y un valor umbral. La función debe retornar una nueva lista plana (un solo nivel) que contenga solo aquellos elementos de la matriz que sean estrictamente mayores al umbral, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [10, 15, 20]
# hint: Puedes recorrer la matriz usando bucles anidados para acceder a cada elemento, almacenarlos en una lista simple y luego aplicar el método sort() o la función sorted().

# === SOLUTION ===
def filtrar_y_ordenar(matriz, umbral):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > umbral:
                resultado.append(elemento)
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert filtrar_y_ordenar([[1, 20], [15, 3], [10, 5]], 8) == [10, 15, 20], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar([[0, 0], [0, 0]], 5) == [], "Error: considera casos donde ningún elemento supera el umbral."
    assert filtrar_y_ordenar([[10, 2], [5, 8]], 1) == [2, 5, 8, 10], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")