# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una lista de palabras y devuelva un diccionario donde las llaves sean las palabras y los valores sean la cantidad de veces que aparece cada una en la lista.
# difficulty: Básico
# expected_output: {'manzana': 2, 'pera': 1}
# hint: Puedes iterar sobre la lista y verificar si la palabra ya existe en el diccionario antes de incrementar su contador o inicializarlo en 1.

# === SOLUTION ===
def contar_frecuencias(lista_palabras):
    frecuencias = {}
    for palabra in lista_palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencias(["hola", "mundo", "hola"]) == {"hola": 2, "mundo": 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencias(["a", "a", "a", "b"]) == {"a": 3, "b": 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencias([]) == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")