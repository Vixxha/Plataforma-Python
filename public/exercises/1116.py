# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto, limpie los signos de puntuación básicos y devuelva un diccionario donde las claves sean las palabras en minúsculas y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Intermedio
# expected_output: {"hola": 2, "mundo": 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras y el método .split() para separar el texto por espacios. Recuerda verificar si la palabra ya existe en el diccionario antes de incrementar su contador.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    
    # Eliminar puntuación básica y convertir a minúsculas
    for caracter in string.punctuation:
        texto = texto.replace(caracter, "")
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo, hola Python") == {"hola": 2, "mundo": 1, "python": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Test... test! TEST.") == {"test": 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")