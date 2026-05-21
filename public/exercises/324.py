# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz (lista de listas) de números enteros, devuelve una nueva matriz donde todos los valores menores a 0 se reemplacen por 0, y todos los valores mayores a 10 se reemplacen por 10.
# difficulty: Intermedio
# expected_output: [[0, 5, 10], [2, 10, 0]]
# hint: Puedes iterar sobre las filas con un bucle for y, dentro, usar otro bucle o una comprensión de listas para transformar cada elemento.

# === SOLUTION ===
def normalizar_matriz(matriz):
    resultado = []
    for fila in matriz:
        nueva_fila = []
        for valor in fila:
            if valor < 0:
                nueva_fila.append(0)
            elif valor > 10:
                nueva_fila.append(10)
            else:
                nueva_fila.append(valor)
        resultado.append(nueva_fila)
    return resultado

# === TESTS ===
try:
    assert normalizar_matriz([[-5, 5, 15], [2, 12, -1]]) == [[0, 5, 10], [2, 10, 0]], "Error: el test 1 ha fallado."
    assert normalizar_matriz([[10, 0], [11, -1]]) == [[10, 0], [10, 0]], "Error: considera casos límites en tu lógica."
    assert normalizar_matriz([[5, 5], [5, 5]]) == [[5, 5], [5, 5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")