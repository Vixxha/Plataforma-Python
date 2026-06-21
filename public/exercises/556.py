# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra de la frase.
# difficulty: Básico
# expected_output: "OTAN" para la entrada "Organización del Tratado del Atlántico Norte"
# hint: Usa los métodos .split() para separar las palabras y un bucle o comprensión de listas para extraer el primer carácter de cada una.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Organización del Tratado del Atlántico Norte") == "ODTDAN", "Error: el test 1 ha fallado."
    assert generar_acronimo("computación en la nube") == "CELN", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("inteligencia artificial") == "IA", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")