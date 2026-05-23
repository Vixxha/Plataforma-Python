# === METADATA ===
# title: Analizador de Acrónimos
# description: Crea una función que tome una cadena de texto (frase) y devuelva su acrónimo en mayúsculas. El acrónimo se forma tomando la primera letra de cada palabra.
# difficulty: Básico
# expected_output: "OTAN" para la entrada "Organización del Tratado del Atlántico Norte"
# hint: Usa el método split() para convertir la frase en una lista de palabras y luego itera sobre ellas para extraer el primer carácter.

# === SOLUTION ===
def generar_acronimo(frase):
    palabras = frase.split()
    acronimo = "".join([palabra[0].upper() for palabra in palabras])
    return acronimo

# === TESTS ===
try:
    assert generar_acronimo("Organización del Tratado del Atlántico Norte") == "ODTDAN", "Error: el test 1 ha fallado."
    assert generar_acronimo("inteligencia artificial") == "IA", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("python es divertido") == "PED", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")