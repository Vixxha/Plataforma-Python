# === METADATA ===
# title: Filtrar y Multiplicar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y un número entero multiplicador. La función debe retornar una nueva matriz donde solo se mantengan las filas cuya suma total sea mayor o igual a 10, y además, todos los elementos de esas filas seleccionadas deben ser multiplicados por el valor dado.
# difficulty: Intermedio
# expected_output: [[6, 8], [10, 12, 14]]
# hint: Puedes recorrer la matriz usando un bucle o compresión de listas, calculando la suma de cada fila antes de decidir si se incluye y se transforma.

# === SOLUTION ===
def filtrar_y_multiplicar_matriz(matriz, multiplicador):
    resultado = []
    for fila in matriz:
        if sum(fila) >= 10:
            fila_modificada = [elemento * multiplicador for elemento in fila]
            resultado.append(fila_modificada)
    return resultado

# === TESTS ===
try:
    assert filtrar_y_multiplicar_matriz([[1, 2], [5, 5], [3, 4]], 2) == [[10, 10], [6, 8]], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar_matriz([[1, 1], [2, 2]], 3) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar_matriz([[4, 6], [1, 1, 1]], 1) == [[4, 6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")