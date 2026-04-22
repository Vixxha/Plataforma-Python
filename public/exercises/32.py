# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que reciba una cadena de texto y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra, ignorando espacios adicionales.
# difficulty: Intermedio
# expected_output: "NASA" para la entrada "National Aeronautics and Space Administration"
# hint: Utiliza el método split() para separar las palabras y accede al primer carácter de cada una.

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("National Aeronautics and Space Administration") == "NASA", "Error: el test 1 ha fallado."
    assert generar_acronimo("as soon as possible") == "ASAP", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("objetos orientados a programacion") == "OOAP", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")