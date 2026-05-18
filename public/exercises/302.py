# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva una cadena compuesta por la primera letra de cada palabra en mayúsculas.
# difficulty: Básico
# expected_output: "UAM" para la entrada "Universidad Autonoma Metropolitana"
# hint: Considera utilizar el método split() para separar las palabras y un bucle o comprensión de listas para extraer el primer carácter de cada una.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("universidad autonoma metropolitana") == "UAM", "Error: el test 1 ha fallado."
    assert generar_acronimo("objetos orientados a objetos") == "OOAO", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("python") == "P", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")