# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Dada una matriz de números enteros (lista de listas), escribe una función que devuelva una lista plana con todos los elementos que sean mayores que 10, normalizados (divididos) por el valor del máximo elemento de la matriz original.
# difficulty: Intermedio
# expected_output: [0.2, 0.4, 0.8]
# hint: Primero encuentra el valor máximo de toda la matriz, luego recorre la estructura para filtrar y dividir simultáneamente.

# === SOLUTION ===
def procesar_matriz(matriz):
    if not matriz or not any(matriz):
        return []
    
    max_val = max(max(fila) for fila in matriz)
    resultado = []
    
    for fila in matriz:
        for elemento in fila:
            if elemento > 10:
                resultado.append(elemento / max_val)
                
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[5, 20], [10, 40]]) == [0.5, 1.0], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 2], [3, 4]]) == [], "Error: no debe incluir elementos menores o iguales a 10."
    assert procesar_matriz([[50, 100], [25, 10]]) == [0.5, 1.0, 0.25], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")