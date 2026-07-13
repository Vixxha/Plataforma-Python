# === METADATA ===
# title: Filtrado y Normalización de Matrices
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos sean reemplazados por 0, y todos los valores positivos sean normalizados restándoles el valor mínimo de toda la matriz.
# difficulty: Intermedio
# expected_output: [[0, 2, 0], [1, 5, 0]] para input [[-5, 3, -1], [2, 6, -2]] con min=-1
# hint: Primero encuentra el valor mínimo de toda la matriz recorriéndola. Luego, usa una comprensión de listas anidada para crear la nueva matriz aplicando la lógica de reemplazo.

# === SOLUTION ===
def procesar_matriz(matriz):
    if not matriz or not matriz[0]:
        return matriz
    
    # Encontrar el valor mínimo de toda la matriz
    min_val = min(min(fila) for fila in matriz)
    
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = []
        for x in fila:
            if x < 0:
                nueva_fila.append(0)
            else:
                nueva_fila.append(x - min_val)
        nueva_matriz.append(nueva_fila)
        
    return nueva_matriz

# === TESTS ===
try:
    assert procesar_matriz([[-5, 3, -1], [2, 6, -2]]) == [[0, 4, 0], [3, 7, 0]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 2], [3, 4]]) == [[0, 1], [2, 3]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[-1, -2], [-3, -4]]) == [[0, 0], [0, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")