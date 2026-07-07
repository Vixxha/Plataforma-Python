# === METADATA ===
# title: Filtrado y Normalización de Matrices
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos sean reemplazados por 0 y los valores superiores a 100 sean reemplazados por 100.
# difficulty: Intermedio
# expected_output: [[0, 50, 100], [10, 0, 100]]
# hint: Puedes iterar a través de las filas y luego a través de los elementos de cada fila usando un bucle anidado o una lista de comprensión.

# === SOLUTION ===
def normalizar_matriz(matriz):
    resultado = []
    for fila in matriz:
        nueva_fila = []
        for valor in fila:
            if valor < 0:
                nueva_fila.append(0)
            elif valor > 100:
                nueva_fila.append(100)
            else:
                nueva_fila.append(valor)
        resultado.append(nueva_fila)
    return resultado

# === TESTS ===
try:
    assert normalizar_matriz([[-5, 50, 150], [10, -1, 200]]) == [[0, 50, 100], [10, 0, 100]], "Error: el test 1 ha fallado."
    assert normalizar_matriz([[0, 100], [50, 50]]) == [[0, 100], [50, 50]], "Error: considera casos límites en tu lógica."
    assert normalizar_matriz([[]]) == [[]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")