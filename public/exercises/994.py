# === METADATA ===
# title: Conteo de Frecuencias de Palabras
# description: Escribe una función que tome una cadena de texto (oración), cuente cuántas veces aparece cada palabra y devuelva un diccionario con las palabras como claves y sus frecuencias como valores. La función debe ignorar las diferencias entre mayúsculas y minúsculas (convirtiendo todo a minúsculas) y eliminar los signos de puntuación básicos comunes como comas y puntos.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para las mayúsculas, .replace() o .strip() para limpiar los signos de puntuación, y .split() para separar la cadena en una lista de palabras.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    if not texto.strip():
        return {}
    
    # Limpiar puntuación básica y convertir a minúsculas
    puntuacion = [',', '.', '!', '?', ';', ':']
    texto_limpio = texto.lower()
    for p in puntuacion:
        texto_limpio = texto_limpio.replace(p, '')
        
    palabras = texto_limpio.split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo, hola Python.") == {'hola': 2, 'mundo': 1, 'python': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python python PYTHON") == {'python': 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")