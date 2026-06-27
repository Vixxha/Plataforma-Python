# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva una cadena con las iniciales de cada palabra en mayúsculas, unidas sin espacios.
# difficulty: Básico
# expected_output: "UFO" para "Unidentified Flying Object"
# hint: Usa el método .split() para obtener las palabras de la cadena y luego recorre la lista resultante para extraer el primer carácter de cada una.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Unidentified Flying Object") == "UFO", "Error: el test 1 ha fallado."
    assert generar_acronimo("as soon as possible") == "ASAP", "Error: considera casos con minúsculas."
    assert generar_acronimo("NASA") == "N", "Error: el caso de una sola palabra falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")