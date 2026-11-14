# === METADATA ===
# title: Conteo y Búsqueda de Frecuencias de Palabras
# description: Escribe una función que tome una cadena de texto, cuente la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y puntuación básica como comas y puntos) usando un diccionario, y devuelva la palabra que más se repite. Si hay un empate, devuelve cualquiera de ellas en minúscula.
# difficulty: Intermedio
# expected_output: "python"
# hint: Puedes usar .lower(), .replace() para limpiar el texto, y .split() para separar las palabras. Luego, recorre el diccionario para encontrar la clave con el valor máximo.

# === SOLUTION ===
def palabra_mas_frecuente(texto):
    import string
    
    # Limpiar el texto de puntuación y pasarlo a minúsculas
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    
    palabras = texto.lower().split()
    
    if not palabras:
        return ""
    
    # Contar frecuencias usando un diccionario
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    # Encontrar la palabra con mayor frecuencia
    max_palabra = max(frecuencias, key=frecuencias.get)
    return max_palabra

# === TESTS ===
try:
    assert palabra_mas_frecuente("Python es genial. Me encanta programar en Python, sí, PYTHON.") == "python", "Error: el test 1 ha fallado."
    assert palabra_mas_frecuente("perro gato perro") == "perro", "Error: considera casos límites en tu lógica."
    assert palabra_mas_frecuente("hola mundo") == "hola", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")