# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra.
# difficulty: Básico
# expected_output: "UAM" para "Universidad Autonoma Metropolitana"
# hint: Utiliza el método .split() para dividir la frase en una lista de palabras y luego itera sobre ellas para extraer el primer carácter.

# === SOLUTION ===
def crear_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert crear_acronimo("Universidad Autonoma Metropolitana") == "UAM", "Error: el test 1 ha fallado."
    assert crear_acronimo("objetos orientados a objetos") == "OOAO", "Error: considera casos límites en tu lógica."
    assert crear_acronimo("python es genial") == "PEG", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")