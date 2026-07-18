# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada una en el texto (ignorando mayúsculas y signos de puntuación).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .lower() para normalizar el texto, .split() para separar palabras y un bucle para actualizar el contador en el diccionario.

# === SOLUTION ===
def contar_frecuencia(texto):
    import re
    # Limpiar el texto de signos de puntuación y convertir a minúsculas
    limpio = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = limpio.split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo, hola.") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("Python es genial y Python es fácil") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'fácil': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")