# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva una cadena compuesta por la primera letra de cada palabra en mayúsculas.
# difficulty: Básico
# expected_output: "UFO"
# hint: Utiliza el método .split() para separar la cadena en una lista de palabras y luego recorre esa lista extrayendo el primer carácter de cada elemento.

# === SOLUTION ===
def obtener_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert obtener_acronimo("objetos identificados no identificados") == "OINI", "Error: el test 1 ha fallado."
    assert obtener_acronimo("as soon as possible") == "ASAP", "Error: considera casos límites en tu lógica."
    assert obtener_acronimo("inteligencia artificial") == "IA", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")