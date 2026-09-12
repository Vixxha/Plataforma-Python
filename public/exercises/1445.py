# === METADATA ===
# title: Conteo y Búsqueda de Palabras Frecuentes
# description: Escribe una función que tome una lista de strings (palabras), cuente la frecuencia de cada una utilizando un diccionario y devuelva la palabra que más se repite. Si hay un empate, debe devolver la palabra que aparezca primero alfabéticamente o la primera encontrada según la lógica de conteo.
# difficulty: Intermedio
# expected_output: "manzana"
# hint: Puedes iterar sobre la lista para poblar un diccionario con las frecuencias y luego usar la función max() pasando una clave personalizada que evalúe tanto la frecuencia como la palabra.

# === SOLUTION ===
def palabra_mas_frecuente(palabras):
    if not palabras:
        return None
    
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
        
    # Encontramos la palabra con mayor frecuencia. 
    # Para manejar empates de forma determinista, podemos ordenar por frecuencia descendente y palabra ascendente.
    max_palabra = max(conteo, key=lambda x: (conteo[x], -ord(x[0]) if x else 0))
    
    # Una forma más estándar y limpia para el nivel es buscar el max usando la frecuencia como clave principal
    # y el orden inverso de la palabra para desempatar si se requiere, o simplemente la primera ocurrencia.
    # Usemos una aproximación directa y robusta:
    frecuencia_maxima = max(conteo.values())
    candidatas = [p for p, freq in conteo.items() if freq == frecuencia_maxima]
    
    # Retornamos la primera alfabéticamente en caso de empate para que sea determinista
    return sorted(candidatas)[0]

# === TESTS ===
try:
    assert palabra_mas_frecuente(["manzana", "pera", "manzana", "uva", "pera", "manzana"]) == "manzana", "Error: el test 1 ha fallado."
    assert palabra_mas_frecuente(["sol", "luna", "sol", "luna", "mar"]) == "luna", "Error: considera casos límites en tu lógica."
    assert palabra_mas_frecuente(["python"]) == "python", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")