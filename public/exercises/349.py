# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es "perfecto". Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo el número mismo).
# difficulty: Intermedio
# expected_output: True para 6, False para 8
# hint: Un número es perfecto si la suma de sus divisores desde 1 hasta n/2 es igual al número original.

# === SOLUTION ===
def es_numero_perfecto(n):
    if n < 2:
        return False
    suma_divisores = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

# === TESTS ===
try:
    assert es_numero_perfecto(6) == True, "Error: el 6 es un número perfecto (1+2+3=6)."
    assert es_numero_perfecto(28) == True, "Error: el 28 es un número perfecto (1+2+4+7+14=28)."
    assert es_numero_perfecto(8) == False, "Error: el 8 no es un número perfecto."
    assert es_numero_perfecto(1) == False, "Error: el caso base 1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")