# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores negativos (errores de sensor) y devuelva una nueva lista con las temperaturas restantes convertidas a grados Fahrenheit (F = C * 9/5 + 32), redondeadas a un decimal.
# difficulty: Intermedio
# expected_output: [50.0, 68.0, 86.0]
# hint: Puedes usar una lista por comprensión (list comprehension) para filtrar y transformar los datos en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(lista_celsius):
    return [round(c * 9/5 + 32, 1) for c in lista_celsius if c >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([10, 20, 30]) == [50.0, 68.0, 86.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-5, 0, 10]) == [32.0, 50.0], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([-10, -20]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")