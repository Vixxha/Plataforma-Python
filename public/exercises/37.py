# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de aparición de cada palabra (considerando las palabras en minúsculas y eliminando signos de puntuación básicos como comas y puntos).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .replace() para limpiar el texto, .split() para obtener una lista de palabras y un diccionario para ir acumulando los conteos.

# === SOLUTION ===
def contar_frecuencia(texto):
    texto = texto.lower().replace(',', '').replace('.', '')
    palabras = texto.split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo, hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("Python es genial. Python es divertido.") == {'python': 2, 'es': 2, 'genial': 1, 'divertido': 1}, "Error: considera casos con signos de puntuación."
    assert contar_frecuencia("") == {}, "Error: el caso base de string vacío falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")