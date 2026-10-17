# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto, cuente cuántas veces aparece cada palabra (ignorando mayúsculas/minúsculas y puntuación básica como comas o puntos) y devuelva un diccionario con los resultados.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para estandarizar el texto y .split() para separar las palabras, además de .strip(".,") para limpiar la puntuación.

# === SOLUTION ===
def contar_palabras(texto):
    texto_limpio = texto.lower().replace(",", "").replace(".", "")
    palabras = texto_limpio.split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_palabras("Hola mundo, hola Python.") == {"hola": 2, "mundo": 1, "python": 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Test test TEST.") == {"test": 3}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")