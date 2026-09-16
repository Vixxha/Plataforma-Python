# === METADATA ===
# title: Operaciones de Transposición y Promedio en una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una tupla con dos elementos: 1) La matriz transpuesta (intercambiando filas por columnas), y 2) El promedio de todos los elementos contenidos en la matriz original redondeado a 2 decimales. Si la matriz está vacía, debe retornar una tupla vacía: ().
# difficulty: Intermedio
# expected_output: (([[1, 4], [2, 5], [3, 6]], 3.5)
# hint: Puedes recorrer la matriz usando bucles anidados o comprensiones de lista para la transposición, y sumar todos los elementos contando el total para el promedio.

# === SOLUTION ===
def procesar_matriz(matriz):
    if not matriz or not matriz[0]:
        return ()
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Transponer matriz
    transpuesta = [[matriz[f][c] for f in range(filas)] for c in range(columnas)]
    
    # Calcular promedio
    total_elementos = filas * columnas
    suma_total = sum(sum(fila) for fila in matriz)
    promedio = round(suma_total / total_elementos, 2)
    
    return (transpuesta, promedio)

# === TESTS ===
try:
    assert procesar_matriz([[1, 2, 3], [4, 5, 6]]) == ([[1, 4], [2, 5], [3, 6]], 3.5), "Error: el test 1 ha fallado."
    assert procesar_matriz([[10, 20], [30, 40]]) == ([[10, 30], [20, 40]], 25.0), "Error: considera casos límites en tu lógica."
    assert procesar_matriz([]) == (), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")