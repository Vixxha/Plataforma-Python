# === METADATA ===
# title: Filtrar y Multiplicar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y un número entero multiplicador. La función debe devolver una nueva matriz donde solo se mantengan las filas cuya suma total sea un número par, y además, cada elemento de esas filas filtradas debe ser multiplicado por el valor dado.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]]
# hint: Puedes recorrer la matriz fila por fila, calcular la suma de cada una usando la función sum(), comprobar si es par usando el operador módulo (%), y si cumple, multiplicar sus elementos antes de agregarlos a la nueva matriz.

# === SOLUTION ===
def filtrar_y_multiplicar_matriz(matriz, multiplicador):
    resultado = []
    for fila in matriz:
        if sum(fila) % 2 == 0:
            fila_modificada = [elemento * multiplicador for elemento in fila]
            resultado.append(fila_modificada)
    return resultado

# === TESTS ===
try:
    assert filtrar_y_multiplicar_matriz([[1, 2], [3, 3]], 2) == [[6, 6]], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar_matriz([[1, 1], [2, 2], [3, 4]], 3) == [[3, 3], [6, 6]], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar_matriz([[1, 3], [5, 7]], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")