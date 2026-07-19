# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una lista de cadenas de texto y devuelva un diccionario donde las llaves sean las palabras y los valores sean la cantidad de veces que cada palabra aparece en la lista.
# difficulty: Básico
# expected_output: {'apple': 2, 'banana': 1, 'orange': 1}
# hint: Puedes iterar sobre la lista y verificar si la palabra ya existe como llave en el diccionario para incrementar su valor o inicializarlo en 1.

# === SOLUTION ===
def contar_frecuencia(lista_palabras):
    frecuencia = {}
    for palabra in lista_palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia(["apple", "banana", "apple", "orange"]) == {'apple': 2, 'banana': 1, 'orange': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia(["a", "a", "a"]) == {'a': 3}, "Error: considera casos con elementos repetidos."
    assert contar_frecuencia([]) == {}, "Error: el caso de una lista vacía debe devolver un diccionario vacío."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")