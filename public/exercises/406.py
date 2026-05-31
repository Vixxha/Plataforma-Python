# === METADATA ===
# title: Analizador de Palíndromos Limpio
# description: Crea una función que reciba una cadena, elimine todos los espacios y signos de puntuación, convierta todo a minúsculas y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# difficulty: Intermedio
# expected_output: True o False
# hint: Usa el método .isalnum() para filtrar caracteres y considera el slicing [::-1] para invertir la cadena.

# === SOLUTION ===
def es_palindromo_limpio(texto):
    # Filtrar solo caracteres alfanuméricos y convertir a minúsculas
    limpio = "".join(char.lower() for char in texto if char.isalnum())
    # Comparar la cadena con su versión invertida
    return limpio == limpio[::-1]

# === TESTS ===
try:
    assert es_palindromo_limpio("Anita lava la tina") == True, "Error: el test 1 ha fallado."
    assert es_palindromo_limpio("Hola Mundo") == False, "Error: considera casos límites en tu lógica."
    assert es_palindromo_limpio("A man, a plan, a canal: Panama") == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")