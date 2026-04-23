# === METADATA ===
# title: Filtrado y Normalización de Matrices
# description: Dada una matriz (lista de listas) de números enteros, implementa una función que devuelva una nueva lista con todos los elementos de la matriz que sean mayores a 10, pero elevados al cuadrado.
# difficulty: Intermedio
# expected_output: [121, 144, 400]
# hint: Puedes utilizar una lista por comprensión anidada o dos bucles 'for' para recorrer la matriz y aplicar la condición antes de realizar la operación.

# === SOLUTION ===
def procesar_matriz(matriz):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > 10:
                resultado.append(elemento ** 2)
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[5, 11], [12, 8], [20, 2]]) == [121, 144, 400], "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 2], [3, 4]]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[10, 15], [20, 5]]) == [225, 400], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")