# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dado una lista de temperaturas (números enteros), crea una función que elimine todas las temperaturas inferiores a 0 grados y, posteriormente, devuelva una nueva lista con los valores restantes escalados multiplicándolos por 1.1.
# difficulty: Intermedio
# expected_output: [11.0, 22.0, 33.0]
# hint: Puedes usar una lista por comprensión (list comprehension) para filtrar y transformar los datos en una sola línea de código.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [temp * 1.1 for temp in temperaturas if temp >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([10, -5, 20, -1, 30]) == [11.0, 22.0, 33.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-10, -20, -30]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([0, 100]) == [0.0, 110.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")