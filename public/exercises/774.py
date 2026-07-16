# === METADATA ===
# title: Analizador de Acrónimos Invertidos
# description: Crea una función que reciba una cadena de palabras, extraiga la primera letra de cada palabra (en mayúsculas), las concatene y devuelva el resultado invertido.
# difficulty: Básico
# expected_output: "PTC" para la entrada "Codificación de Python"
# hint: Usa el método split() para separar las palabras, un bucle para obtener las iniciales y el slicing [::-1] para invertir la cadena final.

# === SOLUTION ===
def obtener_acronimo_invertido(texto):
    palabras = texto.split()
    acronimo = "".join([p[0].upper() for p in palabras])
    return acronimo[::-1]

# === TESTS ===
try:
    assert obtener_acronimo_invertido("Python es genial") == "G E P"[:5].replace(" ", "").upper()[::-1] # Ejemplo: "G E P" -> "GEP" -> "PEG"
    assert obtener_acronimo_invertido("programacion orientada a objetos") == "AOPO"
    assert obtener_acronimo_invertido("inteligencia artificial") == "IA"[::-1]
    assert obtener_acronimo_invertido("Hola") == "H"
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")