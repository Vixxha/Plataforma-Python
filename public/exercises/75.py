# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz (lista de listas) de números enteros, escribe una función que devuelva una nueva lista plana con todos los elementos que sean mayores a un umbral dado, pero normalizados (divididos por el valor máximo presente en la matriz original).
# difficulty: Intermedio
# expected_output: [0.2, 0.6, 1.0] para una matriz [[1, 3], [5, 0]] con umbral 0.
# hint: Primero encuentra el valor máximo de toda la matriz, luego recorre la estructura anidada para filtrar y calcular el valor normalizado.

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
    assert filtrar_y_normalizar([[1, 3], [5, 2]], 2) == [0.6, 1.0], "Error: el test 1 ha fallado."
    assert filtrar_y_normalizar([[10, 20], [30, 40]], 25) == [0.75, 1.0], "Error: considera casos límites en tu lógica."
    assert filtrar_y_normalizar([[5, 5], [5, 5]], 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")