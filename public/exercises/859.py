# === METADATA ===
# title: Conteo de Frecuencias de Palabras
# description: Escribe una función que tome una cadena de texto (oración), cuente cuántas veces aparece cada palabra y devuelva un diccionario con los resultados. La función debe ignorar las diferencias entre mayúsculas y minúsculas (convirtiendo todo a minúsculas) y los signos de puntuación básicos como comas y puntos.
# difficulty: Básico-Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método `.lower()` para las minúsculas, `.replace()` para quitar puntuación y el método `.split()` para separar las palabras.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    # Eliminar signos de puntuación básicos
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    
    # Convertir a minúsculas y separar en palabras
    palabras = texto.lower().split()
    
    # Construir el diccionario de frecuencias
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo, hola Python.") == {'hola': 2, 'mundo': 1, 'python': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python es genial. ¡Sí, Python!") == {'python': 2, 'es': 1, 'genial': 1, 'sí': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("Test") == {'test': 1}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")