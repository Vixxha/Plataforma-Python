# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas, extrayendo la primera letra de cada palabra.
# difficulty: Básico
# expected_output: "NASA" para la entrada "National Aeronautics and Space Administration"
# hint: Usa el método .split() para separar las palabras y un bucle o comprensión de lista para obtener los caracteres.

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("National Aeronautics and Space Administration") == "NASA", "Error: el test 1 ha fallado."
    assert generar_acronimo("objetos orientados a programacion") == "OOAP", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("Hola mundo") == "HM", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")