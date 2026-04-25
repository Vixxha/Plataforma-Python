# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores negativos y devuelva una nueva lista con los valores restantes escalados restando el promedio de la lista original a cada elemento. Redondea los resultados a 2 decimales.
# difficulty: Intermedio
# expected_output: [1.25, 2.25, -0.75]
# hint: Primero calcula el promedio de la lista original, luego filtra los positivos y finalmente aplica la operación aritmética usando una lista por comprensión.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    filtradas = [t for t in temperaturas if t >= 0]
    resultado = [round(t - promedio, 2) for t in filtradas]
    return resultado

# === TESTS ===
try:
    assert procesar_temperaturas([10, 20, 5]) == [-3.33, 6.67, -8.33], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([0, 10, -5]) == [-1.67, 8.33], "Error: considera casos límites en tu lógica."
    assert procesar_temperaturas([100]) == [0.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")