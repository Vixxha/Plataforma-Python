# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, cuente la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y puntuación básica) y devuelva un diccionario donde las claves sean las palabras y los valores sean la cantidad de veces que aparecen.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras y reemplazar signos de puntuación antes de usar .split() para separar el texto.

# === SOLUTION ===
def contar_palabras(texto):
    import string
    # Eliminar puntuación y pasar a minúsculas
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
    assert contar_palabras("Hola mundo, hola Python") == {'hola': 2, 'mundo': 1, 'python': 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Test. Test! test?") == {'test': 3}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")