# === METADATA ===
# title: Analizador de Acrónimos y Formato
# description: Escribe una función que reciba una cadena de texto, elimine los espacios extra al inicio y final, convierta todo a mayúsculas y devuelva una lista con las iniciales de cada palabra.
# difficulty: Intermedio
# expected_output: ['P', 'L', 'P']
# hint: Utiliza los métodos .strip(), .split() y una comprensión de listas para extraer el primer carácter de cada elemento.

# === SOLUTION ===
def generar_acronimo(texto):
    palabras = texto.strip().split()
    return [palabra[0].upper() for palabra in palabras]

# === TESTS ===
try:
    assert generar_acronimo("  programacion lenguaje python  ") == ['P', 'L', 'P'], "Error: el test 1 ha fallado."
    assert generar_acronimo("inteligencia artificial") == ['I', 'A'], "Error: considera casos límites en tu lógica."
    assert generar_acronimo("  hola  ") == ['H'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")