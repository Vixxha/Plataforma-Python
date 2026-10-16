# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que reciba un texto (string), elimine la puntuación básica, lo divida en palabras y devuelva un diccionario donde las claves sean las palabras en minúsculas y los valores sean la cantidad de veces que aparecen en el texto.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras, .split() para separar el texto y un diccionario (o collections.Counter) para almacenar las frecuencias.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    
    # Eliminar signos de puntuación
    for char in string.punctuation:
        texto = texto.replace(char, "")
        
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola python") == {"hola": 2, "mundo": 1, "python": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python, python. PYTHON!") == {"python": 3}, "Error: considera casos límites en tu lógica (mayúsculas y puntuación)."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base (string vacío) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")