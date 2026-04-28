# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto y devuelva una cadena compuesta por la primera letra de cada palabra en mayúsculas.
# difficulty: Básico
# expected_output: "NASA" para la entrada "National Aeronautics and Space Administration"
# hint: Utiliza el método split() para separar las palabras y asegúrate de convertir cada carácter inicial a mayúsculas con .upper().

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("National Aeronautics and Space Administration") == "NASA", "Error: el test 1 ha fallado."
    assert generar_acronimo("objetivo de desarrollo sostenible") == "ODS", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("python") == "P", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")