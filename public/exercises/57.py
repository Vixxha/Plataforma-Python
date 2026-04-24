# === METADATA ===
# title: Filtrado de Valores en Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y un umbral, y devuelva una lista plana (vector) con todos los números de la matriz que sean estrictamente mayores al umbral, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [15, 20, 25] si la entrada es [[1, 10], [25, 15, 5], [20]] con umbral 10.
# hint: Puedes recorrer la matriz usando un bucle anidado o una comprensión de listas, y luego aplicar el método .sort() o la función sorted().

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
    assert filtrar_y_ordenar_matriz([[1, 10], [25, 15, 5], [20]], 10) == [15, 20, 25], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_matriz([[5, 5], [5, 5]], 10) == [], "Error: considera casos donde ningún elemento cumple la condición."
    assert filtrar_y_ordenar_matriz([[100, 2], [30, 40]], 0) == [2, 30, 40, 100], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")