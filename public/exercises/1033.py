# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto, limpie los signos de puntuación básicos y cuente la frecuencia de cada palabra, devolviendo un diccionario donde las claves son las palabras en minúsculas y los valores son la cantidad de veces que aparecen.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras, y reemplazar o eliminar puntuación antes de usar .split() para separar el texto.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    # Eliminar puntuación
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation))
    # Convertir a minúsculas y separar por espacios
    palabras = texto_limpio.lower().split()
    
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo, hola Python.") == {'hola': 2, 'mundo': 1, 'python': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Uno, dos, dos, tres, tres, tres.") == {'uno': 1, 'dos': 2, 'tres': 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")