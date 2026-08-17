# === METADATA ===
# title: Filtrar y Multiplicar Matriz
# description: Dada una matriz de números enteros (lista de listas) y un número escalar, devuelve una nueva matriz donde todos los elementos que sean múltiplos del escalar hayan sido reemplazados por el valor 0, y los demás se mantengan igual.
# difficulty: Intermedio
# expected_output: [[1, 0, 3], [0, 5, 0]]
# hint: Puedes recorrer la matriz usando bucles anidados o una list comprehension, evaluando cada elemento con el operador módulo (%).

# === SOLUTION ===
def filtrar_multiplos_matriz(matriz, escalar):
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            if elemento % escalar == 0:
                nueva_fila.append(0)
            else:
                nueva_fila.append(elemento)
        nueva_matriz.append(nueva_fila)
    return nueva_matriz

# === TESTS ===
try:
    assert filtrar_multiplos_matriz([[1, 2, 3], [4, 5, 6]], 2) == [[1, 0, 3], [0, 5, 0]], "Error: el test 1 ha fallado."
    assert filtrar_multiplos_matriz([[10, 15], [20, 25]], 5) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert filtrar_multiplos_matriz([[7, 11], [13, 17]], 3) == [[7, 11], [13, 17]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")