# === METADATA ===
# title: Frecuencia de Caracteres
# description: Crea una función que reciba una cadena de texto y retorne un diccionario donde las llaves sean los caracteres y los valores sean la cantidad de veces que cada carácter aparece en la cadena.
# difficulty: Básico
# expected_output: {'h': 1, 'o': 2, 'l': 1, 'a': 1} para 'hola'
# hint: Itera sobre la cadena y verifica si el carácter ya existe como llave en el diccionario antes de incrementar su contador.

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
    assert contar_frecuencia("banana") == {'b': 1, 'a': 3, 'n': 2}, "Error: considera casos con letras repetidas."
    assert contar_frecuencia("") == {}, "Error: el caso base de cadena vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")