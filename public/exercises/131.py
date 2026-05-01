# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz (lista de listas) de números enteros, escribe una función que devuelva una nueva lista con todos los elementos de la matriz que sean mayores a 10, pero elevados al cuadrado.
# difficulty: Intermedio
# expected_output: [144, 225, 400]
# hint: Puedes usar un bucle anidado para recorrer las filas y columnas, o una comprensión de lista (list comprehension) para hacerlo de forma más concisa.

# === SOLUTION ===
def procesar_matriz(matriz):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > 10:
                resultado.append(elemento ** 2)
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[5, 12], [8, 15], [20, 2]]) == [144, 225, 400], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 2], [3, 4]]) == [], "Error: considera casos donde ningún elemento cumple la condición."
    assert procesar_matriz([[11, 10], [9, 100]]) == [121, 10000], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")