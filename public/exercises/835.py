# === METADATA ===
# title: Conteo de Frecuencias de Palabras
# description: Escribe una función que tome una cadena de texto, cuente la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y puntuación básica) y devuelva un diccionario con las palabras como claves y sus frecuencias como valores.
# difficulty: Intermedio
# expected_output: {"hola": 2, "mundo": 1}
# hint: Puedes usar el método .lower() y reemplazar signos de puntuación, además de iterar sobre .split() actualizando el diccionario con el método .get().

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    
    # Limpiar puntuación y pasar a minúsculas
    texto_limpio = texto.lower()
    for signo in string.punctuation:
        texto_limpio = texto_limpio.replace(signo, "")
    
    palabras = texto_limpio.split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo, hola Python.") == {"hola": 2, "mundo": 1, "python": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Test de prueba, test de prueba.") == {"test": 2, "de": 2, "prueba": 2}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")