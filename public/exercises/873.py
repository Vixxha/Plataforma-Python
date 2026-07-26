# === METADATA ===
# title: Validador de Acrónimos Automáticos
# description: Escribe una función que tome una frase en formato string y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra de la frase. Ignora los espacios dobles si los hubiera.
# difficulty: Básico
# expected_output: "Organización de Aviación Civil Internacional" -> "OACI"
# hint: Puedes usar el método .split() para separar las palabras por espacios y luego iterar sobre ellas para extraer el primer carácter.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Organización de Aviación Civil Internacional") == "OACI", "Error: el test 1 ha fallado."
    assert generar_acronimo("objetivo de desarrollo sostenible") == "ODS", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("Hyper Text Markup Language") == "HTML", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")