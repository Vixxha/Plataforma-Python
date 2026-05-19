# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra, ignorando mayúsculas y signos de puntuación básicos.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Puedes usar el método .lower() para normalizar el texto y .split() para separar las palabras. Considera eliminar signos de puntuación usando .replace().

# === SOLUTION ===
def contar_palabras(texto):
    import re
    # Limpiar el texto: convertir a minúsculas y quitar puntuación
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto_limpio.split()
    frecuencia = {}
    
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
        
    return frecuencia

# === TESTS ===
try:
    assert contar_palabras("Hola mundo, hola.") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Python es genial, Python es útil.") == {'python': 2, 'es': 2, 'genial': 1, 'útil': 1}, "Error: considera la normalización de mayúsculas."
    assert contar_palabras("") == {}, "Error: el caso base (cadena vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")