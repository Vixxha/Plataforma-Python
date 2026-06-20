# === METADATA ===
# title: Verificador de Números Perfectos
# description: Crea una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel cuya suma de sus divisores propios (excluyéndose a sí mismo) es igual al propio número.
# difficulty: Intermedio
# expected_output: True para 6 (1+2+3=6), False para 8.
# hint: Itera desde 1 hasta la mitad del número dado y acumula aquellos divisores cuyo residuo al dividir sea cero.

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
    assert es_numero_perfecto(6) == True, "Error: el 6 es un número perfecto."
    assert es_numero_perfecto(28) == True, "Error: el 28 debe ser detectado como perfecto."
    assert es_numero_perfecto(12) == False, "Error: el 12 no es un número perfecto."
    assert es_numero_perfecto(1) == False, "Error: el caso base 1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")