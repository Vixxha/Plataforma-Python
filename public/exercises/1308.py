# === METADATA ===
# title: Conteo de Frecuencias de Palabras
# description: Escribe una función que tome una cadena de texto, cuente la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y puntuación básica) y devuelva un diccionario con los resultados.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Puedes usar .lower() para estandarizar las palabras y .split() para separarlas, luego recorre el resultado actualizando un diccionario.

# === SOLUTION ===
def contar_palabras(texto):
    import string
    # Limpiar puntuación y convertir a minúsculas
    for caracter in string.punctuation:
        texto = texto.replace(caracter, "")
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_palabras("Hola mundo, hola Python") == {"hola": 2, "mundo": 1, "python": 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Test... test! TEST.") == {"test": 3}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")