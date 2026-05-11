# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas. El acrónimo debe estar formado por la primera letra de cada palabra.
# difficulty: Básico
# expected_output: "UFO" para "Unidentified Flying Object"
# hint: Utiliza el método split() para separar las palabras y recorre cada palabra para extraer el primer carácter.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Unidentified Flying Object") == "UFO", "Error: el test 1 ha fallado."
    assert generar_acronimo("as soon as possible") == "ASAP", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("NASA") == "N", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")