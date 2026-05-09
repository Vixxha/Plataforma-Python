# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde solo se conserven los números pares, sustituyendo los impares por 0, y finalmente devuelva la matriz transpuesta (las filas se convierten en columnas).
# difficulty: Intermedio
# expected_output: [[2, 0], [4, 6]] para la entrada [[2, 5], [0, 6], [4, 1]] (tras filtrado previo)
# hint: Primero recorre la matriz para aplicar la lógica de los números pares, luego utiliza el truco de 'zip(*matriz)' para trasponerla fácilmente.

# === SOLUTION ===
def filtrar_y_trasponer(matriz):
    # Filtrar pares y convertir impares a 0
    filtrada = [[num if num % 2 == 0 else 0 for num in fila] for fila in matriz]
    
    # Trasponer la matriz usando zip
    traspuesta = [list(columna) for columna in zip(*filtrada)]
    
    return traspuesta

# === TESTS ===
try:
    assert filtrar_y_trasponer([[1, 2], [3, 4]]) == [[0, 0], [2, 4]], "Error: el test 1 ha fallado."
    assert filtrar_y_trasponer([[1, 3, 5], [2, 4, 6]]) == [[0, 2], [0, 4], [0, 6]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_trasponer([[10]]) == [[10]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")