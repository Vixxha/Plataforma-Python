# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, cuente la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y puntuación básica) y devuelva un diccionario con los resultados.
# difficulty: Intermedio
# expected_output: {'python': 2, 'es': 1, 'genial': 1}
# hint: Puedes usar el método .lower() y reemplazar signos como comas o puntos antes de usar .split() para separar las palabras.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    
    # Limpiar puntuación y convertir a minúsculas
    texto_limpio = texto.lower()
    for signo in string.punctuation:
        texto_limpio = texto_limpio.replace(signo, '')
        
    palabras = texto_limpio.split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Python es genial y Python es divertido.") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'divertido': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Hola, hola. ¿Cómo estás?") == {'hola': 2, 'cómo': 1, 'estás': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")