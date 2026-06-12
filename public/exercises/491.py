# === METADATA ===
# title: Filtrado de matriz y producto escalar
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y un número escalar. La función debe devolver una nueva matriz donde cada elemento original haya sido multiplicado por el escalar, pero solo si el elemento es un número par. Si el número es impar, debe permanecer como 0 en la matriz resultante.
# difficulty: Intermedio
# expected_output: [[0, 6, 0], [12, 0, 18]]
# hint: Utiliza comprensión de listas anidada o bucles for para iterar sobre las filas y columnas, verificando la paridad con el operador módulo (%).

# === SOLUTION ===
def procesar_matriz(matriz, escalar):
    resultado = []
    for fila in matriz:
        nueva_fila = [(elemento * escalar) if elemento % 2 == 0 else 0 for elemento in fila]
        resultado.append(nueva_fila)
    return resultado

# === TESTS ===
try:
    assert procesar_matriz([[1, 2, 3], [4, 5, 6]], 3) == [[0, 6, 0], [12, 0, 18]], "Error: el test 1 ha fallado."
    assert procesar_matriz([[10, 11], [12, 13]], 2) == [[20, 0], [24, 0]], "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[1, 3], [5, 7]], 10) == [[0, 0], [0, 0]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")