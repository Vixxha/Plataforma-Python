# === METADATA ===
# title: Conteo de Frecuencias de Palabras
# description: Escribe una función que reciba una cadena de texto, limpie los signos de puntuación básicos y devuelva un diccionario donde las claves sean las palabras en minúscula y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras y .split() para separar el texto por espacios. Recuerda verificar o eliminar signos de puntuación comunes como comas o puntos.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    # Eliminar signos de puntuación básicos
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo, hola Python!") == {"hola": 2, "mundo": 1, "python": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Manzana pera manzana plátano PERA manzana") == {"manzana": 3, "pera": 2, "plátano": 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")