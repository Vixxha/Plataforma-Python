# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Crea una función que reciba una matriz (lista de listas) y devuelva una nueva matriz donde solo se incluyan las columnas cuyo primer elemento sea mayor a 10.
# difficulty: Intermedio
# expected_output: [[15, 20], [12, 18], [11, 14]]
# hint: Puedes usar la función zip(*matriz) para iterar sobre las columnas de la matriz original.

# === SOLUTION ===
def filtrar_columnas_mayores_a_diez(matriz):
    if not matriz or not matriz[0]:
        return []
    
    columnas = list(zip(*matriz))
    columnas_filtradas = [list(col) for col in columnas if col[0] > 10]
    
    if not columnas_filtradas:
        return []
    
    # Transponer de nuevo a formato de filas
    return [list(fila) for fila in zip(*columnas_filtradas)]

# === TESTS ===
try:
    assert filtrar_columnas_mayores_a_diez([[15, 5, 20], [12, 2, 18], [11, 3, 14]]) == [[15, 20], [12, 18], [11, 14]], "Error: el test 1 ha fallado."
    assert filtrar_columnas_mayores_a_diez([[5, 2], [1, 1]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_columnas_mayores_a_diez([[10, 11], [10, 11]]) == [[11], [11]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")