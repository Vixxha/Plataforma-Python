# === METADATA ===
# title: Analizador de Hashtags
# description: Escribe una función que tome una cadena de texto que representa un tweet o frase, extraiga todas las palabras que comienzan con el símbolo '#' (hashtags), elimine dicho símbolo, convierta todas las palabras resultantes a minúsculas y las devuelva en una lista ordenada alfabéticamente.
# difficulty: Intermedio
# expected_output: ['python', 'programacion', 'tutorial']
# hint: Puedes usar el método .split() para separar el texto por espacios y verificar si cada palabra empieza con '#'. Recuerda usar .lower() y .sort() o sorted().

# === SOLUTION ===
def extraer_hashtags(texto):
    palabras = texto.split()
    hashtags = []
    for palabra in palabras:
        if palabra.startswith('#') and len(palabra) > 1:
            hashtag_limpio = palabra.lstrip('#').lower()
            # Limpiar posibles signos de puntuación pegados al final
            hashtag_limpio = ''.join(c for c in hashtag_limpio if c.isalnum())
            if hashtag_limpio:
                hashtags.append(hashtag_limpio)
    return sorted(list(set(hashtags)))

# === TESTS ===
try:
    assert extraer_hashtags("Amo aprender #Python y la #Programacion web. ¡Grande #PYTHON!") == ['programacion', 'python'], "Error: el test 1 ha fallado."
    assert extraer_hashtags("Hoy no hay etiquetas de ningun tipo.") == [], "Error: considera casos límites en tu lógica."
    assert extraer_hashtags("#hola #MUNDO #PYTHON_3") == ['hola', 'mundo', 'python3'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")