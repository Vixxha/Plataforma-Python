# === METADATA ===
# title: Analizador de Hashtags
# description: Escribe una función que tome una frase, extraiga todas las palabras que comienzan con el símbolo '#' y devuelva una lista con estas palabras en minúsculas y ordenadas alfabéticamente. Si no hay hashtags, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: ['python', 'programacion', 'tutorial']
# hint: Puedes usar el método .split() para separar el texto en palabras, y luego verificar cuáles empiezan con '#'.

# === SOLUTION ===
def extraer_hashtags(texto):
    palabras = texto.split()
    hashtags = [p.lower() for p in palabras if p.startswith('#')]
    return sorted(hashtags)

# === TESTS ===
try:
    assert extraer_hashtags("Amo aprender #Python y la #Programacion en este #tutorial") == ['programacion', 'python', 'tutorial'], "Error: el test 1 ha fallado."
    assert extraer_hashtags("Sin etiquetas por aquí") == [], "Error: considera casos límites en tu lógica."
    assert extraer_hashtags("#PYTHON #codigo #Python") == ['#codigo', '#python'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")