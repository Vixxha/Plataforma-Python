# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de aparición de cada palabra (considerando las palabras en minúsculas y sin signos de puntuación).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Usa el método .split() para obtener las palabras y un diccionario para ir acumulando los conteos.

# === SOLUTION ===
def contar_frecuencias(texto):
    import re
    palabras = re.findall(r'\w+', texto.lower())
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencias("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencias("Python es genial, Python es divertido.") == {'python': 2, 'es': 2, 'genial': 1, 'divertido': 1}, "Error: considera casos con puntuación."
    assert contar_frecuencias("") == {}, "Error: el caso base de cadena vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")