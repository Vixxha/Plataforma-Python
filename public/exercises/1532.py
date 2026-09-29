# === METADATA ===
# title: Analizador de Hashtags
# description: Escribe una función que reciba una frase o texto, extraiga todas las palabras que comiencen con el símbolo '#' (hashtags), elimine el símbolo, convierta cada hashtag a minúsculas y los devuelva en una lista ordenada alfabéticamente.
# difficulty: Intermedio
# expected_output: ['python', 'programacion', 'tutorial']
# hint: Puedes usar el método .split() para separar el texto en palabras, y luego verificar con .startswith() y manipular la cadena.

# === SOLUTION ===
def extraer_hashtags(texto):
    palabras = texto.split()
    hashtags = []
    for palabra in palabras:
        # Limpiamos posibles signos de puntuación pegados al final del hashtag
        palabra_limpia = palabra.strip(".,!?;:")
        if palabra_limpia.startswith('#') and len(palabra_limpia) > 1:
            tag = palabra_limpia[1:].lower()
            if tag not in hashtags:
                hashtags.append(tag)
    return sorted(hashtags)

# === TESTS ===
try:
    assert extraer_hashtags("Me encanta #Python y la #PROGRAMACION web. ¡Vamos con #python!") == ['programacion', 'python'], "Error: el test 1 ha fallado."
    assert extraer_hashtags("No hay hashtags aqui") == [], "Error: considera casos límites en tu lógica."
    assert extraer_hashtags("#Zeta #alfa #Beta") == ['alfa', 'beta', 'zeta'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")