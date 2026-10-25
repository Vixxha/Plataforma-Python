# === METADATA ===
# title: Analizador de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, cuente la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y puntuación básica) y devuelva un diccionario con las palabras como claves y sus frecuencias como valores.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Puedes usar .lower() para estandarizar las palabras y .split() para separarlas, además de verificar si la palabra ya existe en el diccionario.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    # Eliminar puntuación y pasar a minúsculas
    for caracter in string.punctuation:
        texto = texto.replace(caracter, "")
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python, python. PYTHON!") == {"python": 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")