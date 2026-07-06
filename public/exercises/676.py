# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores extremos (menores a -10 o mayores a 40) y devuelva una nueva lista con las temperaturas restantes convertidas a grados Fahrenheit (F = C * 9/5 + 32).
# difficulty: Intermedio
# expected_output: [50.0, 68.0, 86.0] para la entrada [10, 20, 30, -50, 60]
# hint: Utiliza una lista de comprensión (list comprehension) para filtrar y transformar los datos en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [temp * 9/5 + 32 for temp in temperaturas if -10 <= temp <= 40]

# === TESTS ===
try:
    assert procesar_temperaturas([0, 20, 40]) == [32.0, 68.0, 104.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-20, 50, 10]) == [50.0], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([-10, 40]) == [14.0, 104.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")