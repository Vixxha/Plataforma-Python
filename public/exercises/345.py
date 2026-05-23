# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra de la frase.
# difficulty: Básico
# expected_output: "UML" (para la entrada "Unified Modeling Language")
# hint: Puedes usar el método .split() para dividir la frase en palabras y luego recorrerlas para extraer el primer carácter de cada una.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Unified Modeling Language") == "UML", "Error: el test 1 ha fallado."
    assert generar_acronimo("as soon as possible") == "ASAP", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("objetivo de desarrollo sostenible") == "ODS", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")