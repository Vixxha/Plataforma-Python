# === METADATA ===
# title: Validador de Cadenas Inversas (Palíndromos Simples)
# description: Escribe una función que reciba una cadena de texto, elimine todos los espacios en blanco, la convierta a minúsculas y determine si se lee igual de izquierda a derecha que de derecha a izquierda (es un palíndromo). La función debe devolver True si es un palíndromo y False en caso contrario.
# difficulty: Básico
# expected_output: True
# hint: Puedes usar los métodos de string como .replace(), .lower() y la técnica de slicing [::-1] para invertir cadenas.

# === SOLUTION ===
def es_palindromo(texto):
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo("Python") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo("A man a plan a canal Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")