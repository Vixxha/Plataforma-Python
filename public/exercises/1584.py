# === METADATA ===
# title: Conteo y Búsqueda de Frecuencias de Palabras
# description: Escribe una función que tome una cadena de texto (oración), cuente la frecuencia de cada palabra sin distinguir entre mayúsculas y minúsculas, y devuelva la palabra que aparece con más frecuencia. Si hay un empate, puedes devolver cualquiera de ellas o la primera en orden alfabético.
# difficulty: Intermedio
# expected_output: "python"
# hint: Utiliza un diccionario para almacenar la frecuencia de cada palabra y el método `split()` para separar la oración.

# === SOLUTION ===
def palabra_mas_frecuente(texto):
    if not texto.strip():
        return ""
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    palabra_max = max(frecuencias, key=frecuencias.get)
    return palabra_max

# === TESTS ===
try:
    assert palabra_mas_frecuente("Python es genial y Python es muy util") == "python", "Error: el test 1 ha fallado."
    assert palabra_mas_frecuente("hola mundo hola") == "hola", "Error: considera casos límites en tu lógica."
    assert palabra_mas_frecuente("Un solo test") == "un", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")