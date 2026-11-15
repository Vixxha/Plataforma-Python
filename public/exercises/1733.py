# === METADATA ===
# title: Analizador de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, cuente cuántas veces aparece cada palabra (ignorando mayúsculas y minúsculas) y devuelva un diccionario con las frecuencias. Las puntuaciones comunes deben ser ignoradas o se asume que el texto solo contiene palabras separadas por espacios.
# difficulty: Intermedio
# expected_output: {'python': 2, 'es': 1, 'genial': 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras y el método .split() para separar el texto por espacios.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    if not texto.strip():
        return {}
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Python es genial y Python es divertido") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'divertido': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Hola MUNDO hola") == {'hola': 2, 'mundo': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")