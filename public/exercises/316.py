# === METADATA ===
# title: Filtrado y Normalización de Matrices
# description: Crea una función que reciba una matriz (lista de listas) de números enteros. La función debe retornar una nueva matriz donde todos los números negativos hayan sido reemplazados por 0 y todos los números positivos mayores a 100 hayan sido limitados a 100.
# difficulty: Intermedio
# expected_output: [[0, 50, 100], [20, 0, 100]]
# hint: Puedes usar un bucle anidado para recorrer las filas y columnas, o utilizar comprensión de listas para crear la nueva matriz de forma más concisa.

# === SOLUTION ===
def normalizar_matriz(matriz):
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = []
        for valor in fila:
            if valor < 0:
                nueva_fila.append(0)
            elif valor > 100:
                nueva_fila.append(100)
            else:
                nueva_fila.append(valor)
        nueva_matriz.append(nueva_fila)
    return nueva_matriz

# === TESTS ===
try:
    assert normalizar_matriz([[-5, 50, 150], [20, -10, 100]]) == [[0, 50, 100], [20, 0, 100]], "Error: el test 1 ha fallado."
    assert normalizar_matriz([[200, -200], [50, 50]]) == [[100, 0], [50, 50]], "Error: considera casos límites en tu lógica."
    assert normalizar_matriz([[]]) == [[]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")