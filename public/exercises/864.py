# === METADATA ===
# title: Conteo de Frecuencia de Palabras
# description: Escribe una función que tome una cadena de texto (oración), elimine la sensibilidad a mayúsculas/minúsculas, y devuelva un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra en el texto.
# difficulty: Intermedio
# expected_output: {'python': 2, 'es': 1, 'un': 1, 'lenguaje': 1, 'genial': 1}
# hint: Puedes usar el método .lower() para estandarizar el texto y .split() para separar las palabras. Luego, itera sobre las palabras para poblar el diccionario usando .get(palabra, 0).

# === SOLUTION ===
def contar_frecuencia_palabras(texto):
    if not texto.strip():
        return {}
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# === TESTS ===
try:
    assert contar_frecuencia_palabras("Python es un lenguaje genial y Python es dinamico") == {'python': 2, 'es': 2, 'un': 1, 'lenguaje': 1, 'genial': 1, 'y': 1, 'dinamico': 1}, "Error: el test 1 ha fallado."
    assert contar_frecuencia_palabras("Hola Hola HOLA") == {'hola': 3}, "Error: considera casos límites en tu lógica."
    assert contar_frecuencia_palabras("") == {}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")