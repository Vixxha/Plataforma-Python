# === METADATA ===
# title: Validador de Hashtags y Capitalización
# description: Escribe una función que tome una frase, elimine los espacios en blanco sobrantes, verifique si puede convertirse en un hashtag válido comenzando con '#' y uniendo todas las palabras con la primera letra de cada palabra en mayúscula (formato CamelCase). Si la frase está vacía o excede los 140 caracteres, la función debe devolver False.
# difficulty: Intermedio
# expected_output: "#ProgramacionEnPython"
# hint: Puedes usar los métodos de strings como .split(), .capitalize() y .join(), además de validar la longitud de la cadena resultante.

# === SOLUTION ===
def generar_hashtag(frase):
    if not frase or not frase.strip():
        return False
    
    palabras = frase.strip().split()
    hashtag = "#" + "".join(palabra.capitalize() for palabra in palabras)
    
    if len(hashtag) > 140:
        return False
        
    return hashtag

# === TESTS ===
try:
    assert generar_hashtag("hola mundo python") == "#HolaMundoPython", "Error: el test 1 ha fallado."
    assert generar_hashtag("   aprender a programar es divertido   ") == "#AprenderAProgramarEsDivertido", "Error: considera casos límites en tu lógica."
    assert generar_hashtag("") == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")