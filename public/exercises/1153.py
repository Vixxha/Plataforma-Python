# === METADATA ===
# title: Búsqueda del Tesoro en Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y un número entero que representa el "tesoro". La función debe retornar una tupla con las coordenadas (fila, columna) de la primera aparición del tesoro. Si el tesoro no se encuentra en la matriz, debe retornar la tupla (-1, -1).
# difficulty: Intermedio
# expected_output: (1, 2)
# hint: Puedes usar dos bucles 'for' anidados (o recorrer por índices usando 'range') para examinar cada elemento de la matriz fila por fila.

# === SOLUTION ===
def buscar_tesoro(matriz, tesoro):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == tesoro:
                return (i, j)
    return (-1, -1)

# === TESTS ===
try:
    matriz_ejemplo = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    assert buscar_tesoro(matriz_ejemplo, 60) == (1, 2), "Error: el test 1 ha fallado."
    assert buscar_tesoro(matriz_ejemplo, 10) == (0, 0), "Error: considera casos límites en tu lógica."
    assert buscar_tesoro(matriz_ejemplo, 100) == (-1, -1), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")