# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de aparición de cada palabra (considerando las palabras como minúsculas y omitiendo signos de puntuación básicos).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Puedes usar el método .split() para separar las palabras y un bucle para iterar sobre ellas, actualizando el valor en el diccionario según si la palabra ya existe o no.

# === SOLUTION ===
def contar_frecuencia(texto):
    import re
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto_limpio.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo, hola.") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("Python es genial y Python es divertido") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'divertido': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")