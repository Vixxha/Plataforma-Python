# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, la limpie de puntuación básica o la divida por espacios, y devuelva un diccionario donde las claves sean las palabras únicas (en minúsculas) y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Básico
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras, .split() para separar el texto y el método .get() del diccionario o collections.defaultdict para contar las frecuencias de manera eficiente.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    if not texto.strip():
        return {}
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        # Limpieza básica de signos de puntuación comunes al final o inicio
        palabra limpia = palabra.strip(".,!?;:\"'")
        if palabra_limpia:
            frecuencias[palabra_limpia] = frecuencias.get(palabra_limpia, 0) + 1
            
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python, Python. PYTHON!") == {"python": 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")