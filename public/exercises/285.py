# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Crea una función que reciba una matriz de números enteros (lista de listas) y devuelva una nueva matriz donde todos los valores negativos sean reemplazados por 0, y todos los valores positivos sean normalizados restándoles el valor mínimo de la matriz original.
# difficulty: Intermedio
# expected_output: [[0, 2, 0], [5, 0, 1]]
# hint: Primero identifica el valor mínimo absoluto de todos los elementos de la matriz y luego itera utilizando comprensión de listas o bucles anidados para construir la nueva estructura.

# === SOLUTION ===
def procesar_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    
    # Encontrar el mínimo global para la normalización
    todos_los_valores = [val for fila in matriz for val in fila]
    min_val = min(todos_los_valores)
    
    resultado = []
    for fila in matriz:
        nueva_fila = [max(0, val - min_val) if val >= 0 else 0 for val in fila]
        resultado.append(nueva_fila)
        
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[10, 12, 5], [15, 2, 11]]) == [[5, 7, 0], [10, 0, 6]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[-5, 0], [10, -2]]) == [[0, 5], [15, 0]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[1, 1], [1, 1]]) == [[0, 0], [0, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")