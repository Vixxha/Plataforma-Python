# === METADATA ===
# title: Filtrado y Normalización de Temperaturas
# description: Dada una lista de temperaturas, escribe una función que elimine los valores negativos (errores de sensor) y devuelva una nueva lista con las temperaturas restantes normalizadas, restando a cada una el valor mínimo encontrado en la lista resultante.
# difficulty: Intermedio
# expected_output: [0, 5, 10]
# hint: Primero filtra la lista usando una estructura de control o list comprehension, luego encuentra el valor mínimo y aplica la operación aritmética sobre los elementos filtrados.

# === SOLUTION ===
def procesar_temperaturas(temperaturas):
    filtradas = [t for t in temperaturas if t >= 0]
    if not filtradas:
        return []
    min_val = min(filtradas)
    return [t - min_val for t in filtradas]

# === TESTS ===
try:
    assert procesar_temperaturas([10, -5, 15, 20, -1]) == [0, 5, 10], "Error: el test 1 ha fallado."
    assert procesar_temperaturas([-10, -20]) == [], "Error: el caso con solo negativos debe devolver lista vacía."
    assert procesar_temperaturas([5, 5, 5]) == [0, 0, 0], "Error: el caso de valores iguales falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")