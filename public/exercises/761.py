# === METADATA ===
# title: Analizador de Acrónimos y Formato
# description: Crea una función que reciba una cadena de texto, elimine espacios extra al inicio y final, convierta todo a mayúsculas y extraiga la primera letra de cada palabra para formar un acrónimo.
# difficulty: Básico
# expected_output: "UFO" para " unidentified flying object "
# hint: Usa los métodos .strip(), .split() y un bucle o comprensión de listas para iterar sobre las palabras.

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.strip().split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("  unidentified flying object  ") == "UFO", "Error: el test 1 ha fallado."
    assert generar_acronimo("computational thinking process") == "CTP", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("  python ") == "P", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")