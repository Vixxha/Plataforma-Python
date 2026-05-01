# === METADATA ===
# title: Filtrado y Normalización de Vector
# description: Escribe una función que reciba una lista de números enteros, elimine todos los valores negativos y devuelva una nueva lista donde cada elemento restante sea multiplicado por el valor máximo presente en la lista original.
# difficulty: Intermedio
# expected_output: Para la entrada [1, 2, -5, 4], el resultado debería ser [4, 8, 16]
# hint: Primero identifica el máximo de la lista original usando max() o un bucle, luego usa una lista por comprensión para filtrar y transformar los datos.

# === SOLUTION ===
def procesar_vector(numeros):
    if not numeros:
        return []
    
    max_val = max(numeros)
    return [x * max_val for x in numeros if x >= 0]

# === TESTS ===
try:
    assert procesar_vector([1, 2, -5, 4]) == [4, 8, 16], "Error: el test 1 ha fallado."
    assert procesar_vector([-1, -2, -3]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_vector([0, 5]) == [0, 25], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")