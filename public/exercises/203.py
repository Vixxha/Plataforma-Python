# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra, ignorando mayúsculas y signos de puntuación básicos.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Puedes usar el método .lower() para normalizar el texto y .split() para separar las palabras. Considera eliminar signos de puntuación usando .replace().

# === SOLUTION ===
def contar_frecuencia(texto):
    import re
    # Limpiar el texto de puntuación y convertir a minúsculas
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto_limpio.split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo, hola.") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("Python es genial. Python mola.") == {'python': 2, 'es': 1, 'genial': 1, 'mola': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia("") == {}, "Error: el caso base (string vacío) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")