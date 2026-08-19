# === METADATA ===
# title: Analizador de Acrónimos
# description: Escribe una función que tome una cadena de texto (una frase) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra de la frase. Ignora los espacios adicionales si los hubiera.
# difficulty: Intermedio
# expected_output: "O.T.A.N." (para "Organizacion del Tratado del Atlantico Norte")
# hint: Puedes usar el método .split() para separar las palabras y recorrerlas para extraer su primera letra.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras if palabra])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Organizacion del Tratado del Atlantico Norte") == "ODTAN", "Error: el test 1 ha fallado."
    assert generar_acronimo("objeto de aprendizaje virtual") == "OAV", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("inteligencia artificial") == "IA", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")