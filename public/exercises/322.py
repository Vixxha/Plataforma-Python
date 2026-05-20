# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las llaves sean las palabras y los valores sean la cantidad de veces que aparece cada una. Ignora las mayúsculas/minúsculas.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .lower() para normalizar el texto y .split() para separar las palabras. Puedes usar un bucle o el método .get() para actualizar los contadores.

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Hola mundo hola") == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Python es genial y Python es divertido") == {"python": 2, "es": 2, "genial": 1, "y": 1, "divertido": 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")