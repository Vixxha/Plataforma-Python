# === METADATA ===
# title: Filtrar y Trasponer Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde solo se conserven las filas cuya suma total sea un número par, y además, a dicha matriz resultante se le aplique una transposición (intercambiar filas por columnas). Si ninguna fila cumple la condición, debe retornar una matriz vacía.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]]
# hint: Primero calcula la suma de cada fila para filtrar la matriz original usando una comprensión de lista. Luego, puedes trasponer la matriz resultante utilizando un bucle for anidado o la función zip (*matriz).

# === SOLUTION ===
def filtrar_y_trasponer(matriz):
    if not matriz:
        return []
    
    # Filtrar filas cuya suma sea par
    filas_pares = [fila for fila in matriz if sum(fila) % 2 == 0]
    
    if not filas_pares:
        return []
    
    # Trasponer la matriz resultante
    matriz_transpuesta = [list(columna) for columna in zip(*filas_pares)]
    
    return matriz_transpuesta

# === TESTS ===
try:
    assert filtrar_y_trasponer([[1, 2], [3, 3]]) == [[2, 3]], "Error: el test 1 ha fallado."
    assert filtrar_y_trasponer([[1, 1], [2, 2], [3, 1]]) == [[2], [2]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_trasponer([[1, 3], [5, 7]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")