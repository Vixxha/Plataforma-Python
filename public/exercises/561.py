# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de aparición de cada palabra (considerando las palabras en minúsculas y sin signos de puntuación básicos).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .split() para separar la cadena y un bucle para iterar, actualizando el valor en el diccionario si la palabra ya existe o inicializándola en 1 si es nueva.

# === SOLUTION ===
def contar_frecuencia(texto):
    palabras = texto.lower().replace('.', '').replace(',', '').split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("Python es genial. Python es divertido.") == {'python': 2, 'es': 2, 'genial': 1, 'divertido': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")