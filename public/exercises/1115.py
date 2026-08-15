# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto (oración) y devuelva un diccionario donde las claves sean las palabras únicas (en minúsculas y sin puntuación básica) y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() y .split() para procesar la cadena, y un diccionario o el método .get() para contar las frecuencias.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    texto_limpio = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in texto).lower()
    palabras = texto_limpio.split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python, Python. python!") == {"python": 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")