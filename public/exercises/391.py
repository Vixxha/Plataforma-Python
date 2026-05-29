# === METADATA ===
# title: Filtrado y Normalización de Matrices
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos se conviertan en cero, y cada valor positivo se divida por el valor máximo encontrado en toda la matriz original.
# difficulty: Intermedio
# expected_output: [[0.0, 0.5, 0.0], [1.0, 0.25, 0.0]]
# hint: Primero recorre toda la matriz para encontrar el valor máximo. Luego, usa dos bucles anidados para construir la nueva matriz aplicando la lógica de conversión.

# === SOLUTION ===
def procesar_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    
    max_val = 0
    for fila in matriz:
        for elemento in fila:
            if elemento > max_val:
                max_val = elemento
    
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = []
        for x in fila:
            if x < 0:
                nueva_fila.append(0.0)
            else:
                nueva_fila.append(x / max_val if max_val != 0 else 0.0)
        nueva_matriz.append(nueva_fila)
        
    return nueva_matriz

# === TESTS ===
try:
    assert procesar_matriz([[0, 2, -5], [4, 1, -1]]) == [[0.0, 0.5, 0.0], [1.0, 0.25, 0.0]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[10, 10], [10, 10]]) == [[1.0, 1.0], [1.0, 1.0]], "Error: considera casos con todos los valores iguales."
    assert procesar_matriz([[-1, -2], [-3, -4]]) == [[0.0, 0.0], [0.0, 0.0]], "Error: el caso base de negativos falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")