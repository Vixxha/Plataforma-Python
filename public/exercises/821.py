# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores negativos (errores de sensor) y devuelva una nueva lista con las temperaturas restantes convertidas a grados Celsius. Asume que la lista original está en grados Fahrenheit. La fórmula es: C = (F - 32) * 5/9. Redondea los resultados a 2 decimales.
# difficulty: Intermedio
# expected_output: [10.0, 25.56, 37.78]
# hint: Utiliza una lista por comprensión (list comprehension) para filtrar los elementos mayores o iguales a 0 y aplicar la fórmula de conversión simultáneamente.

# === SOLUTION ===
def procesar_temperaturas(lista_farenheit):
    return [round((f - 32) * 5 / 9, 2) for f in lista_farenheit if f >= 0]

# === TESTS ===
try:
    assert procesar_temperaturas([32, 78, 100, -5, -10]) == [0.0, 25.56, 37.78], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-10, -20]) == [], "Error: debería devolver una lista vacía si todos son negativos."
    assert procesar_temperaturas([32, 212]) == [0.0, 100.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")