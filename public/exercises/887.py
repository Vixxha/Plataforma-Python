# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto, limpie los signos de puntuación básicos y devuelva un diccionario donde las claves sean las palabras en minúsculas y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Intermedio
# expected_output: {'python': 2, 'es': 1, 'genial': 1}
# hint: Puedes usar el método .lower(), .split() y un bucle o el método .get() de los diccionarios para contar las ocurrencias.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    # Eliminar puntuación básica
    for char in string.punctuation:
        texto = texto.replace(char, "")
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Python es genial y Python es facil") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'facil': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Hola hola, MUNDO!") == {'hola': 2, 'mundo': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")