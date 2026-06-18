# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de aparición de cada palabra (considerando las palabras en minúsculas y sin signos de puntuación básicos).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Puedes usar el método .split() para separar las palabras y un bucle para iterar sobre ellas, actualizando el valor en el diccionario si la palabra ya existe o inicializándola en 1 si es nueva.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    palabras = texto.lower().replace('.', '').replace(',', '').split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python es genial, Python es útil.") == {'python': 2, 'es': 2, 'genial': 1, 'útil': 1}, "Error: considera la limpieza de signos."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base (cadena vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")