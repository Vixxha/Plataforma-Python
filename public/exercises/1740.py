# === METADATA ===
# title: Conteo y Búsqueda de Frecuencias de Palabras
# description: Escribe una función que tome una cadena de texto, cuente la frecuencia de aparición de cada palabra (ignorando mayúsculas/minúsculas y puntuación básica) y devuelva la palabra que más se repite. En caso de empate, debe retornar la palabra que aparezca primero alfabéticamente.
# difficulty: Intermedio
# expected_output: "python"
# hint: Puedes usar `.lower()`, `.split()` y un diccionario para almacenar las frecuencias. Para ordenar en caso de empate, recuerda que las claves de un diccionario se pueden ordenar.

# === SOLUTION ===
def palabra_mas_frecuente(texto):
    import string
    
    # Limpiar puntuación y convertir a minúsculas
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palabras = texto_limpio.split()
    
    if not palabras:
        return ""
    
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    # Encontrar la frecuencia máxima
    max_freq = max(frecuencias.values())
    
    # Filtrar palabras con la frecuencia máxima y ordenar alfabéticamente
    candidatas = [palabra for palabra, freq in frecuencias.items() if freq == max_freq]
    
    return sorted(candidatas)[0]

# === TESTS ===
try:
    assert palabra_mas_frecuente("Hola mundo hola Python, mundo.") == "hola", "Error: el test 1 ha fallado."
    assert palabra_mas_frecuente("apple banana apple orange banana apple") == "apple", "Error: considera casos límites en tu lógica."
    assert palabra_mas_frecuente("gato perro gato perro") == "gato", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")