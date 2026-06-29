# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz de números enteros (lista de listas), escribe una función que devuelva una lista plana (vector) con todos los números mayores a 10, multiplicados por 2, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [22, 24, 26, 30]
# hint: Puedes usar un ciclo anidado o list comprehension para recorrer la matriz y el método .sort() para ordenar el resultado final.

# === SOLUTION ===
def filtrar_y_normalizar(matriz):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > 10:
                resultado.append(elemento * 2)
    resultado.sort()
    return resultado

# === TESTS ===
try:
    assert filtrar_y_normalizar([[5, 11, 2], [13, 8, 15], [1, 20]]) == [22, 26, 30, 40], "Error: el test 1 ha fallado."
    assert filtrar_y_normalizar([[1, 2], [3, 4]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_normalizar([[10, 11], [12, 9]]) == [22, 24], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")