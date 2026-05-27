# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra, ignorando mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Convierte el texto a minúsculas y usa el método split() para separar las palabras, luego itera para poblar el diccionario.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python es genial y Python es poderoso") == {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'poderoso': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base (string vacío) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")