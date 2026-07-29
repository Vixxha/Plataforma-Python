# === METADATA ===
# title: Validador de Acrónimos Automáticos
# description: Escribe una función que tome una frase en formato string y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra de la frase. Ignora los espacios dobles si los hubiera.
# difficulty: Intermedio
# expected_output: "Organización de las Naciones Unidas" -> "ONU"
# hint: Puedes usar el método .split() para separar las palabras y luego iterar para extraer sus primeras letras.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Organización de las Naciones Unidas") == "ONU", "Error: el test 1 ha fallado."
    assert generar_acronimo("objetivo de desarrollo sostenible") == "ODS", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("Inteligencia Artificial") == "IA", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")