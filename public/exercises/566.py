# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una lista plana con todos los valores mayores a 10, multiplicados por 2.
# difficulty: Intermedio
# expected_output: [22, 24, 26] para la entrada [[1, 11], [12, 5, 13]]
# hint: Puedes usar un bucle anidado para recorrer la matriz o una comprensión de listas con doble iteración.

# === SOLUTION ===
def procesar_matriz(matriz):
    resultado = []
    for fila in matriz:
        for elemento in fila:
            if elemento > 10:
                resultado.append(elemento * 2)
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[1, 11], [12, 5, 13]]) == [22, 24, 26], "Error: el test 1 ha fallado."
    assert procesar_matriz([[5, 5], [2, 2]]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[20], [10], [30]]) == [40, 60], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")