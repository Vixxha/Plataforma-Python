# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que reciba un string, elimine espacios y signos de puntuación, lo convierta a minúsculas y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# difficulty: Intermedio
# expected_output: True (para "Anita lava la tina") o False (para "Hola mundo")
# hint: Utiliza un bucle o métodos de string para filtrar caracteres alfanuméricos antes de realizar la comparación con el string invertido mediante slicing [::-1].

# === SOLUTION ===
def es_palindromo_limpio(texto):
    texto_limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto_limpio == texto_limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo_limpio("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo_limpio("Hola mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo_limpio("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")