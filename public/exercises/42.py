# === METADATA ===
# title: Filtrado y Normalización de Vector
# description: Crea una función que reciba una lista de números enteros, elimine todos los valores negativos y devuelva una nueva lista donde cada número restante sea dividido por la suma total de los elementos positivos originales.
# difficulty: Intermedio
# expected_output: [0.1, 0.2, 0.7] (Para una entrada [1, 2, 7, -5])
# hint: Primero calcula la suma de los números positivos (filtrando los negativos), luego usa una estructura de repetición o comprensión de listas para normalizar los valores.

# === SOLUTION ===
def normalizar_positivos(lista):
    positivos = [x for x in lista if x > 0]
    total = sum(positivos)
    if total == 0:
        return []
    return [x / total for x in positivos]

# === TESTS ===
try:
    assert normalizar_positivos([1, 2, 7, -5]) == [0.1, 0.2, 0.7], "Error: el test 1 ha fallado."
    assert normalizar_positivos([-1, -2, -3]) == [], "Error: considera casos límites en tu lógica."
    assert normalizar_positivos([10, 10]) == [0.5, 0.5], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")