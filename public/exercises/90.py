# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel cuya suma de sus divisores propios (excluyéndose a sí mismo) es igual al propio número.
# difficulty: Intermedio
# expected_output: True para 6 (1+2+3), False para 8 (1+2+4 = 7)
# hint: Itera desde 1 hasta la mitad del número y acumula los valores que tengan residuo 0 al dividir el número original.

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
    assert es_numero_perfecto(6) == True, "Error: el test 1 ha fallado."
    assert es_numero_perfecto(28) == True, "Error: el test 2 ha fallado."
    assert es_numero_perfecto(12) == False, "Error: el test 3 ha fallado."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")