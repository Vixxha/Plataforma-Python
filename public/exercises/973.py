# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, la limpie de puntuación básica o la divida por espacios, y devuelva un diccionario donde las claves sean las palabras únicas (en minúsculas) y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Intermedio
# expected_output: {'python': 2, 'es': 1, 'genial': 1, 'y': 1, 'divertido': 1}
# hint: Puedes usar el método .lower() para estandarizar las palabras, .split() para separarlas por espacios, y el método .get() del diccionario para contar las ocurrencias de forma elegante.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    if not texto.strip():
        return {}
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        # Limpieza básica de signos de puntuación comunes si es necesario
        palabra_limpia = palabra.strip(".,¡!¿?()[]{}:;")
        if palabra_limpia:
            frecuencias[palabra_limpia] = frecuencias.get(palabra_limpia, 0) + 1
            
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Python es genial y Python es divertido") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'divertido': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Hola, hola. ¿Cómo estás?") == {'hola': 2, 'cómo': 1, 'estás': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")