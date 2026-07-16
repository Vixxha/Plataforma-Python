# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra, ignorando mayúsculas y signos de puntuación básicos.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .lower() para normalizar el texto, .split() para separar palabras y un diccionario para ir acumulando los conteos.

# === SOLUTION ===
import re

def contar_frecuencias(texto):
    palabras = re.findall(r'\b\w+\b', texto.lower())
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencias("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencias("Python es genial, Python es simple.") == {'python': 2, 'es': 2, 'genial': 1, 'simple': 1}, "Error: considera casos con puntuación."
    assert contar_frecuencias("") == {}, "Error: el caso de texto vacío falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")