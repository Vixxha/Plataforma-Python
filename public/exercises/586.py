# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz de números enteros (lista de listas), escribe una función que devuelva una nueva lista que contenga solo los números pares de la matriz, pero multiplicados por dos.
# difficulty: Intermedio
# expected_output: [4, 8, 12] para la entrada [[1, 2], [3, 4], [5, 6]]
# hint: Puedes usar un bucle anidado para recorrer las filas y columnas, o utilizar una comprensión de lista (list comprehension) para filtrar y transformar los datos en una sola línea.

# === SOLUTION ===
def procesar_matriz(matriz):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento % 2 == 0:
                resultado.append(elemento * 2)
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[1, 2], [3, 4], [5, 6]]) == [4, 8, 12], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 3], [5, 7]]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[10, 20], [30, 40]]) == [20, 40, 60, 80], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")