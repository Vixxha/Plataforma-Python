# === METADATA ===
# title: Analizador de Hashtags
# description: Escribe una función que tome una cadena de texto que representa un tweet y devuelva una lista con todas las palabras que actúan como hashtags (es decir, que comienzan con el símbolo '#'). Las palabras devueltas deben incluir el símbolo '#' y estar ordenadas en el orden en que aparecen en el texto.
# difficulty: Básico
# expected_output: ['#python', '#programacion']
# hint: Puedes usar el método .split() para separar el texto por espacios y luego evaluar cada palabra utilizando el operador startswith().

# === SOLUTION ===
def extraer_hashtags(texto):
    palabras = texto.split()
    hashtags = [palabra for palabra in palabras if palabra.startswith('#')]
    return hashtags

# === TESTS ===
try:
    assert extraer_hashtags("Me encanta programar en #python y aprender #programacion todos los días.") == ['#python', '#programacion'], "Error: el test 1 ha fallado."
    assert extraer_hashtags("Hoy no hay etiquetas en este texto.") == [], "Error: considera casos límites en tu lógica."
    assert extraer_hashtags("#Hola #Mundo, esto es una #prueba.") == ['#Hola', '#Mundo', '#prueba.'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")