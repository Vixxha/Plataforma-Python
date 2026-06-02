# === METADATA ===
# title: Frecuencia de Palabras
# description: Escribe una función que reciba una lista de palabras y retorne un diccionario donde las claves sean las palabras y los valores sean la cantidad de veces que cada palabra aparece en la lista.
# difficulty: Básico
# expected_output: {'apple': 2, 'banana': 1, 'orange': 1}
# hint: Puedes iterar sobre la lista y verificar si la palabra ya existe como clave en el diccionario; si no, inicialízala en 1, de lo contrario, incrementa su valor.

# === SOLUTION ===
def contar_frecuencia(lista_palabras):
    frecuencias = {}
    for palabra in lista_palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia(['apple', 'banana', 'apple', 'orange']) == {'apple': 2, 'banana': 1, 'orange': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia(['a', 'a', 'a']) == {'a': 3}, "Error: considera casos con una sola palabra repetida."
    assert contar_frecuencia([]) == {}, "Error: el caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")