# === METADATA ===
# title: Filtrado y Normalización de Matrices
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos sean reemplazados por 0, y todos los valores positivos sean normalizados restándoles el valor mínimo de la matriz original.
# difficulty: Intermedio
# expected_output: [[0, 2, 0], [1, 5, 0]]
# hint: Primero encuentra el valor mínimo de toda la matriz usando bucles anidados o min() con comprensión de listas, luego itera nuevamente para aplicar la transformación.

# === SOLUTION ===
def transformar_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    
    flat_list = [val for fila in matriz for val in fila]
    min_val = min(flat_list)
    
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = []
        for val in fila:
            if val < 0:
                nueva_fila.append(0)
            else:
                nueva_fila.append(val - min_val)
        nueva_matriz.append(nueva_fila)
        
    return nueva_matriz

# === TESTS ===
try:
    assert transformar_matriz([[10, 12, -5], [11, 15, -1]]) == [[0, 2, 0], [1, 5, 0]], "Error: el test 1 ha fallado."
    assert transformar_matriz([[0, 0], [0, 0]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert transformar_matriz([[-1, -2], [3, 4]]) == [[0, 0], [4, 5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")