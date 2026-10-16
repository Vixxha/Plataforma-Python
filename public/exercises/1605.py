# === METADATA ===
# title: Filtrar y Rotar Matriz 1D (Vectores)
# description: Escribe una función que reciba una lista de números enteros y un número entero `k`. La función debe filtrar todos los números pares, y luego rotar los elementos restantes `k` posiciones hacia la derecha. Si `k` es mayor que la longitud de la lista resultante, debe usar el módulo para evitar desbordamientos. Si la lista resultante queda vacía, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [5, 1, 3]
# hint: Primero filtra los elementos usando comprensión de listas y la condición de imparidad (`x % 2 != 0`). Luego, puedes usar slicing para rotar la lista calculando el índice de corte efectivo con `k % len(lista)`.

# === SOLUTION ===
def filtrar_y_rotar(vector, k):
    impares = [x for x in vector if x % 2 != 0]
    if not impares:
        return []
    n = len(impares)
    k = k % n
    if k == 0:
        return impares
    return impares[-k:] + impares[:-k]

# === TESTS ===
try:
    assert filtrar_y_rotar([1, 2, 3, 4, 5, 6], 2) == [3, 5, 1], "Error: el test 1 ha fallado."
    assert filtrar_y_rotar([2, 4, 6, 8], 3) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_rotar([7, 2, 9, 4, 1], 1) == [1, 7, 9], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")