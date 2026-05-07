# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas, extrayendo la primera letra de cada palabra.
# difficulty: Básico
# expected_output: "NASA" para "National Aeronautics and Space Administration"
# hint: Usa el método split() para convertir la frase en una lista de palabras y luego itera sobre ellas para obtener sus iniciales.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("National Aeronautics and Space Administration") == "NASA", "Error: el test 1 ha fallado."
    assert generar_acronimo("objeto orientado a programacion") == "OOAP", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("python") == "P", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")