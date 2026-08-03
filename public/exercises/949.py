# === METADATA ===
# title: Conteo de Frecuencias de Palabras
# description: Escribe una función que reciba una cadena de texto, limpie los signos de puntuación básicos y devuelva un diccionario donde las llaves sean las palabras (en minúsculas) y los valores sean la cantidad de veces que aparecen en el texto.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras, y el método .split() para separar el texto por espacios. Usa el método .get() del diccionario para contar de forma segura.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    
    # Eliminar puntuación
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
    assert contar_frecuencia_palabras("Manzana, pera, MANZANA.") == {"manzana": 2, "pera": 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")