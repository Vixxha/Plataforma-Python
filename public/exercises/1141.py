# === METADATA ===
# title: Búsqueda y Reemplazo en Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros, un valor objetivo y un nuevo valor. La función debe modificar la matriz original (o retornar una nueva) reemplazando todas las ocurrencias del valor objetivo por el nuevo valor, y además retornar la cantidad total de reemplazos realizados.
# difficulty: Intermedio
# expected_output: (Matriz modificada, cantidad_de_reemplazos)
# hint: Puedes recorrer la matriz usando bucles anidados (o por comprensión) para revisar cada elemento y llevar un contador de las veces que se encontró el valor objetivo.

# === SOLUTION ===
def reemplazar_en_matriz(matriz, objetivo, nuevo_valor):
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == objetivo:
                matriz[i][j] = nuevo_valor
                contador += 1
    return matriz, contador

# === TESTS ===
try:
    matriz_test_1 = [[1, 2, 1], [3, 1, 5], [6, 7, 1]]
    res_matriz_1, res_count_1 = reemplazar_en_matriz(matriz_test_1, 1, 9)
    assert res_matriz_1 == [[9, 2, 9], [3, 9, 5], [6, 7, 9]], "Error: el test 1 ha fallado."
    assert res_count_1 == 4, "Error: el conteo de reemplazos es incorrecto."

    matriz_test_2 = [[0, 0], [0, 0]]
    res_matriz_2, res_count_2 = reemplazar_en_matriz(matriz_test_2, 5, 1)
    assert res_matriz_2 == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert res_count_2 == 0, "Error: el conteo de reemplazos para elementos ausentes debe ser 0."

    matriz_test_3 = [[5]]
    res_matriz_3, res_count_3 = reemplazar_en_matriz(matriz_test_3, 5, 8)
    assert res_matriz_3 == [[8]], "Error: el caso base falló."
    assert res_count_3 == 1, "Error: el caso base falló en el conteo."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")