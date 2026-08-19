# === METADATA ===
# title: Analizador de Hashtags
# description: Escribe una función que tome un texto plano, extraiga todas las palabras que comiencen con el símbolo '#' (hashtags), las limpie de cualquier signo de puntuación adyacente y devuelva una lista con los hashtags en minúsculas y ordenados alfabéticamente.
# difficulty: Intermedio
# expected_output: ['python', 'programacion', 'tutorial']
# hint: Usa el método split() para separar las palabras y métodos de string como startswith(), strip() y lower() para limpiarlas.

# === SOLUTION ===
def extraer_hashtags(texto):
    palabras = texto.split()
    hashtags = []
    
    signos_puntuacion = ".,;:!?'\"()[]{}"
    
    for palabra in palabras:
        if palabra.startswith('#') and len(palabra) > 1:
            hashtag_limpio = palabra.strip(signos_puntuacion).lower()
            if hashtag_limpio not in hashtags:
                hashtags.append(hashtag_limpio)
                
    return sorted(hashtags)

# === TESTS ===
try:
    assert extraer_hashtags("Me encanta #Python y la #Programacion. ¡Sigue el #tutorial!") == ['programacion', 'python', 'tutorial'], "Error: el test 1 ha fallado."
    assert extraer_hashtags("No hay hashtags aquí, solo texto normal.") == [], "Error: considera casos límites en tu lógica."
    assert extraer_hashtags("#PYTHON #python #Python") == ['python'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")