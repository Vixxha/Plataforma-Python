# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que reciba una cadena de texto, extraiga la primera letra de cada palabra, la convierta a mayúsculas y devuelva el acrónimo resultante. Ignora espacios extra.
# difficulty: Intermedio
# expected_output: "FBI" para el input "Federal Bureau of Investigation"
# hint: Utiliza el método split() para separar las palabras y un bucle o una comprensión de listas para acceder al primer índice de cada palabra.

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Federal Bureau of Investigation") == "FBOI", "Error: el test 1 ha fallado."
    assert generar_acronimo("objetos orientados a programación") == "OOAP", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("python") == "P", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")