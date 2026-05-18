# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra de la frase.
# difficulty: Básico
# expected_output: "UDL" para "Universidad De Lima"
# hint: Utiliza los métodos .split() para separar las palabras y un bucle o una comprensión de listas para acceder al primer índice de cada palabra.

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Universidad De Lima") == "UDL", "Error: el test 1 ha fallado."
    assert generar_acronimo("objetos orientados a objetos") == "OOAO", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("inteligencia artificial") == "IA", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")