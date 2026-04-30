# === METADATA ===
# title: Verificador de Números Perfectos
# description: Crea una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo el propio número).
# difficulty: Intermedio
# expected_output: True o False
# hint: Un número perfecto es igual a la suma de todos sus divisores menores que él mismo. Puedes iterar desde 1 hasta el número/2 para encontrar los divisores.

# === SOLUTION ===
def es_numero_perfecto(n):
    if n <= 1:
        return False
    suma_divisores = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

# === TESTS ===
try:
    assert es_numero_perfecto(6) == True, "Error: el 6 es el primer número perfecto (1+2+3=6)."
    assert es_numero_perfecto(28) == True, "Error: el 28 debería ser un número perfecto."
    assert es_numero_perfecto(12) == False, "Error: el 12 no es un número perfecto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")