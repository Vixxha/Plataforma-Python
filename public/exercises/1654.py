# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto, limpie los signos de puntuación básicos y cuente la frecuencia de cada palabra, devolviendo un diccionario donde las claves son las palabras en minúsculas y los valores son sus conteos.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'cruel': 1}
# hint: Puedes usar el método .lower(), .split() y reemplazar signos como comas o puntos antes de contar con un diccionario o con collections.Counter.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    # Limpiar signos de puntuación básicos y convertir a minúsculas
    for signo in [".", ",", "!", "?", ";", ":"]:
        texto = texto.replace(signo, "")
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo, hola cruel mundo.") == {'hola': 2, 'mundo': 2, 'cruel': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python python PYTHON") == {'python': 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")