# === METADATA ===
# title: Contador de Frecuencia de Palabras
# description: Crea una función que reciba una cadena de texto y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra en el texto, ignorando mayúsculas y signos de puntuación.
# difficulty: Intermedio
# expected_output: {'hola': 2, 'mundo': 1}
# hint: Utiliza el método .lower() para normalizar el texto y .split() para separar las palabras. Puedes usar un diccionario vacío y un bucle for para iterar y contar.

# === SOLUTION ===
def contar_palabras(texto):
    import re
    # Limpiamos el texto eliminando signos de puntuación y convirtiendo a minúsculas
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto_limpio.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

# === TESTS ===
try:
    assert contar_palabras("Hola mundo, hola.") == {'hola': 2, 'mundo': 1}, "Error: el test 1 ha fallado."
    assert contar_palabras("Python es genial. Python es divertido.") == {'python': 2, 'es': 2, 'genial': 1, 'divertido': 1}, "Error: considera casos límites en tu lógica."
    assert contar_palabras("") == {}, "Error: el caso base (cadena vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")