# === METADATA ===
# title: Analizador de Hashtags
# description: Escribe una función que tome una cadena de texto que representa un tweet o frase, extraiga todas las palabras que comienzan con el símbolo '#' (hashtags), elimine dicho símbolo y devuelva una lista con las palabras resultantes en minúsculas y ordenadas alfabéticamente.
# difficulty: Intermedio
# expected_output: ['python', 'programacion', 'tutorial']
# hint: Puedes usar el método .split() para separar el texto en palabras y verificar si cada palabra comienza con '#'. Recuerda limpiar y formatear cada palabra encontrada.

# === SOLUTION ===
def extraer_hashtags(texto):
    palabras = texto.split()
    hashtags = []
    for palabra in palabras:
        if palabra.startswith('#') and len(palabra) > 1:
            limpio = palabra.strip('.,!?;:').lower()
            if limpio.startswith('#'):
                hashtags.append(limpio[1:])
    return sorted(list(set(hashtags)))

# === TESTS ===
try:
    assert extraer_hashtags("Me encanta #Python y la #Programacion de computadoras. #PYTHON") == ['programacion', 'python'], "Error: el test 1 ha fallado."
    assert extraer_hashtags("Hoy no hay etiquetas aquí, solo texto normal.") == [], "Error: considera casos límites en tu lógica."
    assert extraer_hashtags("#codigo #limpio es #mejor que #codigo #LIMPIO") == ['codigo', 'limpio', 'mejor'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")