# === METADATA ===
# title: Conteo de Frecuencias de Palabras
# description: Escribe una función que tome una cadena de texto, la limpie de signos de puntuación básicos y cuente la frecuencia de cada palabra utilizando un diccionario. La función debe ignorar las mayúsculas/minúsculas (convertir todo a minúsculas) y devolver un diccionario con las palabras como claves y sus frecuencias como valores.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para las minúsculas, .split() para separar las palabras, y el método .get() del diccionario para actualizar los conteos de forma limpia.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    # Eliminar puntuación básica y convertir a minúsculas
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palabras = texto_limpio.split()
    
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola python") == {'hola': 2, 'mundo': 1, 'python': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python, Python! PYTHON.") == {'python': 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")