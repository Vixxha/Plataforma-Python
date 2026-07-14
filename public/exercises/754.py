# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada una en el texto (ignorando mayúsculas).
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1, 'python': 1}
# hint: Puedes usar el método .lower() para normalizar el texto y .split() para dividir la cadena en una lista de palabras.

# === SOLUTION ===
def contar_frecuencia(texto):
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# === TESTS ===
try:
    assert contar_frecuencia("Hola mundo Hola python") == {'hola': 2, 'mundo': 1, 'python': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia("uno dos uno tres dos uno") == {'uno': 3, 'dos': 2, 'tres': 1}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")