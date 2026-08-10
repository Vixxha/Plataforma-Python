# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto (oración), cuente cuántas veces aparece cada palabra (ignorando mayúsculas/minúsculas y signos de puntuación básicos) y devuelva un diccionario con los resultados.
# difficulty: Intermedio
# expected_output: {"hola": 2, "mundo": 1}
# hint: Puedes usar el método .lower() y la función .split() para procesar el texto, y el método .get() del diccionario para contar las ocurrencias de forma elegante.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    import string
    # Limpiar signos de puntuación y convertir a minúsculas
    texto_limpio = texto.lower()
    for signo in string.punctuation:
        texto_limpio = texto_limpio.replace(signo, "")
    
    palabras = texto_limpio.split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python, python. PYTHON!") == {"python": 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")