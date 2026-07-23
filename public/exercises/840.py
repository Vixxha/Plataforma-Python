# === METADATA ===
# title: Conteo de Frecuencias de Palabras
# description: Escribe una función que tome una cadena de texto, la limpie de mayúsculas y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Intermedio
# expected_output: {'python': 2, 'es': 1, 'genial': 1}
# hint: Puedes usar el método .lower() para estandarizar el texto y .split() para separar las palabras por espacios.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Python es genial y Python mola") == {'python': 2, 'es': 1, 'genial': 1, 'y': 1, 'mola': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Hola hola HOLA") == {'hola': 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")