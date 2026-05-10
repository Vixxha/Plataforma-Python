# === METADATA ===
# title: Frecuencia de Caracteres
# description: Crea una función que reciba un string y retorne un diccionario donde las llaves sean los caracteres del string y los valores sean la cantidad de veces que cada carácter aparece en el mismo.
# difficulty: Básico
# expected_output: {'h': 1, 'o': 2, 'l': 1, 'a': 1} para el input 'hola'
# hint: Itera sobre la cadena y verifica si el carácter ya existe como llave en tu diccionario antes de sumar uno.

# === SOLUTION ===
def contar_caracteres(texto):
    frecuencia = {}
    for caracter in texto:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    return frecuencia

# === TESTS ===
try:
    assert contar_caracteres("hola") == {'h': 1, 'o': 1, 'l': 1, 'a': 1}, "Error: el test 1 ha fallado."
    assert contar_caracteres("banana") == {'b': 1, 'a': 3, 'n': 2}, "Error: considera casos con caracteres repetidos."
    assert contar_caracteres("") == {}, "Error: el caso base de string vacío falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")