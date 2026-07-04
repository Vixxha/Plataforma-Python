# === METADATA ===
# title: Analizador de Palabras Palíndromas
# description: Crea una función que reciba un string, elimine espacios y signos de puntuación, lo convierta a minúsculas y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# difficulty: Intermedio
# expected_output: True o False
# hint: Utiliza el método .isalnum() para filtrar caracteres y la técnica de slicing [::-1] para invertir la cadena.

# === SOLUTION ===
def es_palindromo(texto):
    texto_limpio = "".join(char.lower() for char in texto if char.isalnum())
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")