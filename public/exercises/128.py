# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos se conviertan en cero, y cada valor positivo se divida por el máximo valor encontrado en la matriz original. Si la matriz está vacía o el máximo es cero, devuelve la matriz original.
# difficulty: Intermedio
# expected_output: [[0.0, 0.5, 0.0], [1.0, 0.25, 0.0]]
# hint: Primero recorre toda la matriz para hallar el valor máximo absoluto, luego usa una comprensión de listas anidada para transformar los valores.

# === SOLUTION ===
def procesar_matriz(matriz):
    if not matriz or not any(matriz):
        return matriz
    
    plano = [val for fila in matriz for val in fila]
    max_val = max(plano)
    
    if max_val == 0:
        return matriz
    
    return [[max(0.0, float(val) / max_val) for val in fila] for fila in matriz]

# === TESTS ===
try:
    assert procesar_matriz([[0, 2, -5], [4, 1, -2]]) == [[0.0, 0.5, 0.0], [1.0, 0.25, 0.0]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[0, 0], [0, 0]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[-1, -2], [-3, -4]]) == [[0.0, 0.0], [0.0, 0.0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")