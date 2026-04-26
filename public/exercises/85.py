# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dado una lista de temperaturas, escribe una función que elimine los valores negativos (errores de sensor) y devuelva una nueva lista con las temperaturas restantes convertidas de grados Celsius a grados Fahrenheit (F = C * 9/5 + 32).
# difficulty: Intermedio
# expected_output: [68.0, 77.0, 86.0] para una entrada de [-5, 20, 25, 30]
# hint: Puedes usar una lista de comprensión (list comprehension) para filtrar y transformar los datos en una sola línea.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    return [round((t * 9/5) + 32, 2) for t in temperaturas if t >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([-5, 20, 25, 30]) == [68.0, 77.0, 86.0], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-10, -20]) == [], "Error: debería retornar lista vacía al no haber positivos."
    assert procesar_temperaturas([0, 100]) == [32.0, 212.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")