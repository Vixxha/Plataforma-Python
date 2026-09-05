# === METADATA ===
# title: Filtrar y Multiplicar la Diagonal Principal
# description: Escribe una función que reciba una matriz cuadrada (lista de listas) de números enteros. La función debe extraer los elementos de la diagonal principal, filtrar aquellos que sean impares, y multiplicar cada uno de los impares filtrados por su índice original en la diagonal. Finalmente, debe retornar una nueva lista con estos resultados.
# difficulty: Intermedio
# expected_output: [0, 6, 20] para la matriz [[1, 2, 3], [4, 3, 6], [7, 8, 5]] (diagonal: 1 (par/desc), 3 (índice 1 -> 3*1=3 -> espera, 3 es impar: 3*1=3), 5 (índice 2 -> 5*2=10). Ejemplo corregido: para [[2, 2, 3], [4, 3, 6], [7, 8, 5]], la diagonal es [2, 3, 5]. Impares: 3 (en índice 1, 3*1=3), 5 (en índice 2, 5*2=10). Resultado: [3, 10].
# hint: Recorre la matriz usando un bucle con `range(len(matriz))` para acceder a los elementos `matriz[i][i]` y sus índices `i` simultáneamente.

# === SOLUTION ===
def procesar_diagonal(matriz):
    resultado = []
    for i in range(len(matriz)):
        valor = matriz[i][i]
        if valor % 2 != 0:
            resultado.append(valor * i)
    return resultado

# === TESTS ===
try:
    assert procesar_diagonal([[2, 2, 3], [4, 3, 6], [7, 8, 5]]) == [3, 10], "Error: el test 1 ha fallado."
    assert procesar_diagonal([[1, 2], [3, 4]]) == [0], "Error: considera casos límites en tu lógica."
    assert procesar_diagonal([[6, 2], [3, 2]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")