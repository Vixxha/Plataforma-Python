# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas (en minúsculas) y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Básico
# expected_output: {'python': 2, 'es': 1, 'genial': 1}
# hint: Puedes usar el método .lower() para convertir el texto a minúsculas y .split() para separar las palabras.

# === SOLUTION ===
def contar_palabras(texto):
    if not texto.strip():
        return {}
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_palabras("Python es genial") == {"python": 1, "es": 1, "genial": 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Hola hola mundo") == {"hola": 2, "mundo": 1}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")