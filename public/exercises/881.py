# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas (en minúsculas) y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Intermedio
# expected_output: {'python': 2, 'es': 1, 'genial': 1, 'y': 1, 'muy': 1, 'util': 1}
# hint: Puedes usar el método .split() para separar el texto en palabras y .lower() para estandarizarlas.

# === SOLUTION ===
def contar_palabras(texto):
    if not texto.strip():
        return {}
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# === TESTS ===
try:
    assert contar_palabras("Python es genial y Python es muy util") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'muy': 1, 'util': 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Hola hola HOLA") == {'hola': 3}, "Error: considera casos límites en tu lógica (mayúsculas/minúsculas)."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")