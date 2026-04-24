# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas, extrayendo la primera letra de cada palabra.
# difficulty: Básico
# expected_output: "NASA" para "National Aeronautics and Space Administration"
# hint: Usa el método .split() para obtener las palabras de la cadena y luego recorre la lista resultante para extraer el índice cero de cada palabra.

# === SOLUTION ===
def obtener_acronimo(texto):
    palabras = texto.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert obtener_acronimo("National Aeronautics and Space Administration") == "NASA", "Error: el test 1 ha fallado."
    assert obtener_acronimo("objetos orientados a programacion") == "OOAP", "Error: considera casos límites en tu lógica."
    assert obtener_acronimo("python") == "P", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")