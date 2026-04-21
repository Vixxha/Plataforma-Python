# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz de números enteros, escribe una función que devuelva una nueva lista con todos los valores que sean mayores a un umbral dado, pero normalizados (divididos) por el valor máximo de la matriz original.
# difficulty: Intermedio
# expected_output: [0.25, 0.5, 0.75, 1.0]
# hint: Primero encuentra el valor máximo de toda la matriz, luego recorre cada elemento y aplica la condición y la operación matemática.

# === SOLUTION ===
def filtrar_y_normalizar(matriz, umbral):
    if not matriz or not matriz[0]:
        return []
    
    maximo = max(max(fila) for fila in matriz)
    resultado = []
    
    for fila in matriz:
        for elemento in fila:
            if elemento > umbral:
                resultado.append(elemento / maximo)
    
    return resultado

# === TESTS ===
try:
    assert filtrar_y_normalizar([[1, 2], [3, 4]], 1) == [0.5, 0.75, 1.0], "Error: el test 1 ha fallado."
    assert filtrar_y_normalizar([[10, 20], [30, 40]], 25) == [0.75, 1.0], "Error: considera casos límites en tu lógica."
    assert filtrar_y_normalizar([[5, 5], [5, 5]], 10) == [], "Error: el caso base falló (debe retornar lista vacía si nada supera el umbral)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")