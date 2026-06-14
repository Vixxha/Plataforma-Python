# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva una cadena compuesta por la primera letra de cada palabra en mayúsculas.
# difficulty: Básico
# expected_output: "UFO" para "Unidentified Flying Object"
# hint: Utiliza el método .split() para separar las palabras y un bucle o comprensión de lista para extraer el primer carácter.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Unidentified Flying Object") == "UFO", "Error: el test 1 ha fallado."
    assert generar_acronimo("As soon as possible") == "ASAP", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("potable water supply") == "PWS", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")