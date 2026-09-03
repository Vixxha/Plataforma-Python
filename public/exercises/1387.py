# === METADATA ===
# title: Conteo y Búsqueda de Palabras Frecuentes
# description: Escribe una función que reciba una lista de palabras, cuente la frecuencia de cada una utilizando un diccionario, y devuelva la palabra que más se repite. Si hay un empate, debe devolver cualquiera de las más frecuentes o la primera en orden de aparición.
# difficulty: Intermedio
# expected_output: "manzana"
# hint: Puedes recorrer la lista para construir un diccionario de frecuencias y luego usar la función max() especificando una clave personalizada.

# === SOLUTION ===
def palabra_mas_frecuente(palabras):
    if not palabras:
        return None
    
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return max(frecuencias, key=frecuencias.get)

# === TESTS ===
try:
    assert palabra_mas_frecuente(["manzana", "pera", "manzana", "uva", "pera", "manzana"]) == "manzana", "Error: el test 1 ha fallado."
    assert palabra_mas_frecuente(["gato", "perro", "perro", "gato", "ave"]) == "gato", "Error: considera casos límites en tu lógica."
    assert palabra_mas_frecuente(["solo"]) == "solo", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")