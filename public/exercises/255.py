# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas, extrayendo la primera letra de cada palabra.
# difficulty: Básico
# expected_output: "UFO" para "Unidentified Flying Object"
# hint: Usa el método split() para convertir la cadena en una lista de palabras y luego itera sobre ellas.

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Unidentified Flying Object") == "UFO", "Error: el test 1 ha fallado."
    assert generar_acronimo("Portable Network Graphics") == "PNG", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("nacional aeronautics space administration") == "NASA", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")