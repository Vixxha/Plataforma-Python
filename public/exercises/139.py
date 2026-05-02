# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel cuya suma de sus divisores propios (excluyéndose a sí mismo) es igual al número mismo.
# difficulty: Intermedio
# expected_output: True para 6, False para 10
# hint: Itera desde 1 hasta la mitad del número para encontrar sus divisores y acumúlalos en una variable.

# === SOLUTION ===
def es_numero_perfecto(n):
    if n < 2:
        return False
    suma_divisores = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

# === TESTS ===
try:
    assert es_numero_perfecto(6) == True, "Error: el 6 es un número perfecto (1+2+3=6)."
    assert es_numero_perfecto(28) == True, "Error: el 28 es un número perfecto."
    assert es_numero_perfecto(10) == False, "Error: el 10 no es un número perfecto."
    assert es_numero_perfecto(1) == False, "Error: el 1 no debe ser considerado perfecto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")