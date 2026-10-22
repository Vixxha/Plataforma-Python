# === METADATA ===
# title: Analizador de Acrónimos
# description: Escribe una función que tome una frase (string) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra de la frase, ignorando espacios múltiples.
# difficulty: Intermedio
# expected_output: "O.T.A.C." para "Objeto volador no identificado" (o "OVNI" dependiendo de la lógica, pero definamos con puntos o sin puntos claramente. Usemos sin puntos: "OVNI")
# hint: Puedes usar el método .split() para separar las palabras y luego iterar sobre ellas para extraer el primer carácter.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.strip().split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("sistema de posicionamiento global") == "SPG", "Error: el test 1 ha fallado."
    assert generar_acronimo("  control automatico de procesos  ") == "CAP", "Error: considera casos límites en tu lógica y espacios extra."
    assert generar_acronimo("Inteligencia artificial") == "IA", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")