# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que determine si una cadena de texto es un palíndromo, ignorando espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas.
# difficulty: Intermedio
# expected_output: True si la frase se lee igual al revés, False en caso contrario.
# hint: Utiliza métodos de cadena para limpiar el input (como replace o filter) y compara la cadena resultante con su versión invertida usando slicing [::-1].

# === SOLUTION ===
def es_palindromo(texto):
    import string
    limpio = "".join(char.lower() for char in texto if char.isalnum())
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")