# === METADATA ===
# title: Analizador de Acrónimos y Formato
# description: Crea una función que reciba una cadena de texto (frase) y retorne un acrónimo formado por la primera letra de cada palabra en mayúsculas, seguido de la longitud total de la frase original (excluyendo espacios).
# difficulty: Intermedio
# expected_output: ("PPC", 13) para la entrada "Programar Python es Cool"
# hint: Utiliza el método .split() para separar las palabras y recuerda que puedes concatenar strings y medir su longitud con len().

# === SOLUTION ===
def procesar_frase(texto):
    palabras = texto.split()
    acronimo = "".join([p[0].upper() for p in palabras])
    longitud_sin_espacios = len(texto.replace(" ", ""))
    return (acronimo, longitud_sin_espacios)

# === TESTS ===
try:
    assert procesar_frase("Programar Python es Cool") == ("PPEC", 20), "Error: el test 1 ha fallado."
    assert procesar_frase("hola mundo") == ("HM", 9), "Error: considera casos límites en tu lógica."
    assert procesar_frase("A B C") == ("ABC", 3), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")