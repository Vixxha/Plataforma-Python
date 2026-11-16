# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto (oración), cuente la frecuencia de cada palabra ignorando las mayúsculas/minúsculas y devuelva un diccionario con los resultados.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Usa el método .lower() para estandarizar el texto, .split() para separar las palabras y un bucle para ir poblando el diccionario.

# === SOLUTION ===
def contar_palabras(texto):
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_palabras("Hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Python python PYTHON") == {"python": 3}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")