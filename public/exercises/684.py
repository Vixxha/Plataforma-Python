# === METADATA ===
# title: Frecuencia de Caracteres
# description: Implementa una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean los caracteres de la cadena y los valores sean la cantidad de veces que cada carácter aparece en ella.
# difficulty: Básico
# expected_output: {'h': 1, 'o': 2, 'l': 1, 'a': 1}
# hint: Puedes iterar sobre la cadena y verificar si el carácter ya existe en el diccionario antes de incrementar su contador.

# === SOLUTION ===
def contar_frecuencia(cadena):
    frecuencia = {}
    for caracter in cadena:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia("hola") == {'h': 1, 'o': 1, 'l': 1, 'a': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("abracadabra") == {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}, "Error: considera casos con letras repetidas."
    assert contar_frecuencia("") == {}, "Error: el caso de cadena vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")