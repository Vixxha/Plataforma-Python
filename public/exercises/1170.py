# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, cuente la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y puntuación básica) y devuelva un diccionario con los resultados.
# difficulty: Básico
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Puedes usar el método .lower() y .split() para procesar el texto, y el método .get() de los diccionarios para manejar contadores.

# === SOLUTION ===
def contar_palabras(texto):
    import re
    palabras = re.findall(r'\b\w+\b', texto.lower())
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_palabras("Hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Python, python, PYTHON!") == {"python": 3}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")