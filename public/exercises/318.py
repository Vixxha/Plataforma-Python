# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra de la frase.
# difficulty: Básico
# expected_output: "UFO" para "Unidentified Flying Object"
# hint: Utiliza el método split() para separar las palabras y un bucle o una comprensión de listas para extraer el primer carácter de cada una.

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Unidentified Flying Object") == "UFO", "Error: el test 1 ha fallado."
    assert generar_acronimo("sistema de posicionamiento global") == "SDPG", "Error: considera casos con minúsculas."
    assert generar_acronimo("Python") == "P", "Error: el caso de una sola palabra falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")