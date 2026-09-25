# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, cuente cuántas veces aparece cada palabra (ignorando mayúsculas/minúsculas y puntuación básica como comas y puntos) y devuelva un diccionario con los resultados.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras, y .replace() o bucles para eliminar los signos de puntuación antes de usar .split().

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
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
    assert contar_frecuencia_palabras("Hola mundo, hola Python.") == {'hola': 2, 'mundo': 1, 'python': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Rojo, rojo, rojo y azul.") == {'rojo': 3, 'y': 1, 'azul': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("Un solo test.") == {'un': 1, 'solo': 1, 'test': 1}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")