# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra de la frase.
# difficulty: Básico
# expected_output: "CDE" para "Ciencia de datos"
# hint: Utiliza el método .split() para separar la frase en una lista de palabras y luego recorre esa lista extrayendo el índice 0 de cada elemento.

# === SOLUTION ===
def obtener_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert obtener_acronimo("Ciencia de datos") == "CDD", "Error: el test 1 ha fallado."
    assert obtener_acronimo("input output system") == "IOS", "Error: considera casos límites en tu lógica."
    assert obtener_acronimo("Python") == "P", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")