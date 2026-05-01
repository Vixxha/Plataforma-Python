# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz (lista de listas) de números enteros, escribe una función que devuelva una lista unidimensional con todos los números que sean mayores a 10, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [12, 15, 20, 25, 30]
# hint: Puedes recorrer la matriz usando bucles anidados o una comprensión de listas, y luego usar el método .sort() o la función sorted().

# === SOLUTION ===
def filtrar_y_ordenar_matriz(matriz):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > 10:
                resultado.append(elemento)
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert filtrar_y_ordenar_matriz([[1, 15], [20, 5], [12, 30]]) == [12, 15, 20, 30], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_matriz([[5, 2], [8, 9]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_matriz([[10, 11, 25], [10, 10]]) == [11, 25], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")