# === METADATA ===
# title: Analizador de Hashtags
# description: Escribe una función que tome una cadena de texto que representa un tweet o frase, extraiga todas las palabras que comienzan con el símbolo '#' (hashtags), elimine dicho símbolo y devuelva una lista con las palabras resultantes en minúsculas y ordenadas alfabéticamente.
# difficulty: Intermedio
# expected_output: ['python', 'programacion', 'tutorial']
# hint: Puedes usar el método .split() para separar el texto en palabras y verificar si cada palabra comienza con '#'.

# === SOLUTION ===
def extraer_hashtags(texto):
    palabras = texto.split()
    hashtags = []
    for palabra in palabras:
        # Limpiamos posibles signos de puntuación pegados al final del hashtag
        palabra_limpia = palabra.strip(".,!?;:")
        if palabra_limpia.startswith("#") and len(palabra_limpia) > 1:
            hashtags.append(palabra_limpia[1:].lower())
    return sorted(hashtags)

# === TESTS ===
try:
    assert extraer_hashtags("Aprendiendo #Python y #Programacion con este gran #tutorial.") == ['programacion', 'python', 'tutorial'], "Error: el test 1 ha fallado."
    assert extraer_hashtags("No hay hashtags aqui, solo texto plano.") == [], "Error: considera casos límites en tu lógica."
    assert extraer_hashtags("#CODE #Python #code") == ['code', 'code', 'python'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")