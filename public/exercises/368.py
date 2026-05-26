# === METADATA ===
# title: Transformador de Matriz Cuadrada
# description: Dada una matriz (lista de listas) cuadrada de números enteros, escribe una función que devuelva una nueva lista con la suma de cada columna.
# difficulty: Intermedio
# expected_output: [15, 18, 21] para una matriz de 3x3 con números del 1 al 9.
# hint: Puedes iterar sobre los índices de las columnas y, para cada columna, recorrer todas las filas sumando los valores en esa posición.

# === SOLUTION ===
def sumar_columnas(matriz):
    if not matriz or not matriz[0]:
        return []
    
    num_filas = len(matriz)
    num_cols = len(matriz[0])
    resultado = []
    
    for c in range(num_cols):
        suma_columna = 0
        for f in range(num_filas):
            suma_columna += matriz[f][c]
        resultado.append(suma_columna)
        
    return resultado

# === TESTS ===
try:
    assert sumar_columnas([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [12, 15, 18], "Error: el test 1 ha fallado."
    assert sumar_columnas([[10, 0], [0, 10]]) == [10, 10], "Error: considera casos límites en tu lógica."
    assert sumar_columnas([[5]]) == [5], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")