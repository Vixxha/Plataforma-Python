# === METADATA ===
# title: Transformación de Matriz Escalonada
# description: Dada una matriz de números enteros (lista de listas), escribe una función que multiplique cada elemento de la fila 'i' por el valor de 'i + 1'. Por ejemplo, los elementos de la primera fila se multiplican por 1, los de la segunda por 2, y así sucesivamente.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8, 10]] para la entrada [[1, 2], [3, 4, 5]]
# hint: Utiliza un bucle for que recorra los índices de la matriz usando 'enumerate()' para acceder tanto al índice de la fila como a su contenido.

# === SOLUTION ===
def escalar_filas(matriz):
    resultado = []
    for i, fila in enumerate(matriz):
        nuevo_escalar = i + 1
        nueva_fila = [elemento * nuevo_escalar for elemento in fila]
        resultado.append(nueva_fila)
    return resultado

# === TESTS ===
try:
    assert escalar_filas([[1, 2], [3, 4, 5]]) == [[1, 2], [6, 8, 10]], "Error: el test 1 ha fallado."
    assert escalar_filas([[10], [10], [10]]) == [[10], [20], [30]], "Error: considera casos límites en tu lógica."
    assert escalar_filas([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")