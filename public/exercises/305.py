# === METADATA ===
# title: Filtrado y Trasposición de Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, filtre todos los números impares y devuelva una nueva matriz (lista de listas) donde solo se conserven los números pares, manteniendo su posición original relativa. Si en una fila todos los números son impares, esa fila debe quedar vacía.
# difficulty: Intermedio
# expected_output: [[2, 4], [], [6]] para la entrada [[1, 2, 3, 4], [1, 3, 5], [6, 7]]
# hint: Puedes iterar sobre cada fila y, dentro de esta, usar una lista de comprensión para seleccionar solo los números donde 'x % 2 == 0'.

# === SOLUTION ===
def filtrar_matriz_pares(matriz):
    resultado = []
    for fila in matriz:
        fila_filtrada = [num for num in fila if num % 2 == 0]
        resultado.append(fila_filtrada)
    return resultado

# === TESTS ===
try:
    assert filtrar_matriz_pares([[1, 2, 3, 4], [1, 3, 5], [6, 7]]) == [[2, 4], [], [6]], "Error: el test 1 ha fallado."
    assert filtrar_matriz_pares([[1, 3], [5, 7]]) == [[], []], "Error: considera casos límites en tu lógica."
    assert filtrar_matriz_pares([[2, 4, 6], [8, 10]]) == [[2, 4, 6], [8, 10]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")