# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra en el texto (ignorando mayúsculas y signos de puntuación).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .lower() para normalizar el texto, .split() para separar palabras y un diccionario para almacenar los conteos.

# === SOLUTION ===
import re

def contar_palabras(texto):
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto_limpio.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

# === TESTS ===
try:
    assert contar_palabras("Hola mundo, hola.") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Python es genial, Python es simple") == {'python': 2, 'es': 2, 'genial': 1, 'simple': 1}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")