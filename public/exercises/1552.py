# === METADATA ===
# title: Conteo y Búsqueda de Palabras Frecuentes
# description: Escribe una función que tome una lista de palabras, cuente la frecuencia de cada una utilizando un diccionario y devuelva la palabra que más se repite. Si hay un empate, debe devolver cualquiera de ellas, y si la lista está vacía, debe devolver None.
# difficulty: Intermedio
# expected_output: "manzana"
# hint: Puedes usar un bucle para poblar un diccionario con las frecuencias y luego buscar la clave con el valor máximo utilizando la función max() con el argumento key.

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
    assert palabra_mas_frecuente(["manzana", "pera", "manzana", "pera", "manzana"]) == "manzana", "Error: el test 1 ha fallado."
    assert palabra_mas_frecuente(["hola", "mundo", "hola"]) == "hola", "Error: considera casos límites en tu lógica."
    assert palabra_mas_frecuente([]) == None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")