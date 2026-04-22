# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de aparición de cada palabra (considerando las palabras en minúsculas y eliminando signos de puntuación básicos).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .lower() para normalizar, .split() para separar palabras y un diccionario para ir acumulando las cuentas. Puedes usar .strip('.,!?') para limpiar los signos.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    frecuencias = {}
    palabras = texto.lower().split()
    for palabra in palabras:
        palabra_limpia = palabra.strip('.,!?;:')
        if palabra_limpia:
            frecuencias[palabra_limpia] = frecuencias.get(palabra_limpia, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python es genial, genial para programar.") == {'python': 1, 'es': 1, 'genial': 2, 'para': 1, 'programar': 1}, "Error: considera casos con puntuación."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base (cadena vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")