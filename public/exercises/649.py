# === METADATA ===
# title: Verificador de Números Perfectos
# description: Escribe una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al propio número).
# difficulty: Intermedio
# expected_output: True para 6 (1+2+3), False para 8 (1+2+4=7)
# hint: Un número es perfecto si la suma de todos sus divisores menores que él es igual al número mismo. Puedes iterar hasta la mitad del número para encontrar los divisores.

# === SOLUTION ===
def es_numero_perfecto(n):
    if n <= 1:
        return False
    suma_divisores = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

# === TESTS ===
try:
    assert es_numero_perfecto(6) == True, "Error: 6 es un número perfecto."
    assert es_numero_perfecto(28) == True, "Error: 28 es un número perfecto."
    assert es_numero_perfecto(8) == False, "Error: 8 no es un número perfecto."
    assert es_numero_perfecto(1) == False, "Error: El caso base (1) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")