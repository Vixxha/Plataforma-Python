# === METADATA ===
# title: Analizador de Palabras Inversas
# description: Crea una función que tome una oración, invierta el orden de las letras de cada palabra individualmente (manteniendo el orden original de las palabras) y devuelva la nueva cadena resultante.
# difficulty: Intermedio
# expected_output: "olleh dlrow"
# hint: Puedes usar el método .split() para separar las palabras y el slicing [::-1] para invertir cada string.

# === SOLUTION ===
def invertir_palabras(oracion):
    palabras = oracion.split(" ")
    palabras_invertidas = [palabra[::-1] for palabra in palabras]
    return " ".join(palabras_invertidas)

# === TESTS ===
try:
    assert invertir_palabras("hola mundo") == "aloh odnum", "Error: el test 1 ha fallado."
    assert invertir_palabras("Python es genial") == "nohtyP se laineg", "Error: considera casos límites en tu lógica."
    assert invertir_palabras("a b c") == "a b c", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")