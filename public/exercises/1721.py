# === METADATA ===
# title: Filtrar y Multiplicar Vectores
# description: Escribe una función que reciba una lista de números enteros y un número escalar. La función debe retornar una nueva lista donde solo se incluyan los números que sean mayores que el promedio original de la lista, y cada uno de esos números filtrados debe ser multiplicado por el escalar dado. Si la lista está vacía, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [12, 15]
# hint: Primero calcula el promedio sumando todos los elementos y dividiendo por la cantidad. Luego, usa comprensión de listas para filtrar y multiplicar.

# === SOLUTION ===
def filtrar_y_multiplicar(vector, escalar):
    if not vector:
        return []
    
    promedio = sum(vector) / len(vector)
    return [x * escalar for x in vector if x > promedio]

# === TESTS ===
try:
    assert filtrar_y_multiplicar([1, 2, 3, 4, 5], 2) == [8, 10], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar([10, 20, 30], 1) == [20, 30], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar([], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")