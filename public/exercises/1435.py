# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, cuente la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y puntuación básica) y devuelva un diccionario con las palabras como claves y sus frecuencias como valores.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para estandarizar el texto y .split() para separar las palabras, luego itera para llenar el diccionario.

# === SOLUTION ===
def contar_palabras(texto):
    import string
    # Limpiar puntuación y convertir a minúsculas
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palabras = texto_limpio.split()
    
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_palabras("Hola mundo, hola Python!") == {"hola": 2, "mundo": 1, "python": 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Test de prueba, test de PRUEBA.") == {"test": 2, "de": 2, "prueba": 2}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("único") == {"único": 1}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")