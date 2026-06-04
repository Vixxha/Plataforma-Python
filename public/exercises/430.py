# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra.
# difficulty: Básico
# expected_output: "UFO" para "Unidentified Flying Object"
# hint: Utiliza el método .split() para separar las palabras y un bucle o comprensión de listas para obtener los caracteres iniciales.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Unidentified Flying Object") == "UFO", "Error: el test 1 ha fallado."
    assert generar_acronimo("sistema de posicionamiento global") == "SDPG", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("python") == "P", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")