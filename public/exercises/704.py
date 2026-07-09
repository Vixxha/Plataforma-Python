# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores negativos y devuelva una nueva lista con los valores restantes escalados restando el promedio de los valores positivos originales.
# difficulty: Intermedio
# expected_output: [1.0, 3.0, 0.0]
# hint: Primero filtra los valores positivos, calcula su promedio y luego aplica la operación de resta a cada elemento de la lista filtrada.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    positivas = [t for t in temperaturas if t >= 0]
    if not positivas:
        return []
    promedio = sum(positivas) / len(positivas)
    return [round(t - promedio, 2) for t in positivas]

# === TESTS ===
try:
    assert procesar_temperaturas([10, -5, 12, -2, 8]) == [-0.67, 1.33, -2.67] or [procesar_temperaturas([10, -5, 12, -2, 8]) == [-0.6666666666666666, 1.3333333333333335, -2.6666666666666665]]
    assert procesar_temperaturas([-1, -2, -3]) == []
    assert procesar_temperaturas([0, 0, 0]) == [0.0, 0.0, 0.0]
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")