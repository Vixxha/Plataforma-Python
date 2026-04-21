# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos se conviertan en 0 y todos los valores mayores a 10 se conviertan en 10.
# difficulty: Intermedio
# expected_output: [[0, 5, 10], [10, 0, 7]]
# hint: Puedes recorrer la matriz usando bucles anidados o una comprensión de listas doble.

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
    assert normalizar_matriz([[-5, 5, 15], [20, 0, 7]]) == [[0, 5, 10], [10, 0, 7]], "Error: el test 1 ha fallado."
    assert normalizar_matriz([[11, -1], [5, 5]]) == [[10, 0], [5, 5]], "Error: considera casos límites en tu lógica."
    assert normalizar_matriz([[0, 0], [10, 10]]) == [[0, 0], [10, 10]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")