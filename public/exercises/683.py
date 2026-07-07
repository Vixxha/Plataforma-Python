# === METADATA ===
# title: Analizador de Acrónimos y Formatos
# description: Crea una función que tome una cadena de texto, elimine espacios extra al inicio y final, convierta cada palabra a formato Título (primera letra mayúscula) y retorne el acrónimo formado por la primera letra de cada palabra seguido de un guion y el número total de palabras.
# difficulty: Intermedio
# expected_output: "P-O-O-3" (para la entrada "programacion orientada objetos")
# hint: Usa los métodos .strip(), .split() y .title() de las cadenas para procesar el texto antes de construir el resultado.

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.strip().split()
    acronimo = "-".join([p[0].upper() for p in palabras])
    return f"{acronimo}-{len(palabras)}"

# === TESTS ===
try:
    assert generar_acronimo("programacion orientada objetos") == "P-O-O-3", "Error: el test 1 ha fallado."
    assert generar_acronimo("  inteligencia artificial  ") == "I-A-2", "Error: considera casos límites en tu lógica."
    assert generar_acronimo("python") == "P-1", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")