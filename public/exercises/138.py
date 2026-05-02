# === METADATA ===
# title: Filtro y Promedio de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva lista que contenga únicamente los números pares de todas las filas, ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [2, 4, 6, 8]
# hint: Puedes usar un bucle anidado o list comprehension para recorrer la matriz y el operador módulo (%) para identificar los números pares antes de ordenarlos.

# === SOLUTION ===
def filtrar_y_ordenar_pares(matriz):
    pares = []
    for fila in matriz:
        for elemento in fila:
            if elemento % 2 == 0:
                pares.append(elemento)
    return sorted(pares)

# === TESTS ===
try:
    assert filtrar_y_ordenar_pares([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [2, 4, 6, 8], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_pares([[10, 11], [1, 2], [0, 5]]) == [0, 2, 10], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_pares([[1, 3], [5, 7]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")