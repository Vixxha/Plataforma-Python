# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel cuya suma de sus divisores propios (excluyéndose a sí mismo) es igual al número mismo.
# difficulty: Intermedio
# expected_output: True para 6, False para 10
# hint: Itera desde 1 hasta la mitad del número para encontrar sus divisores y acumula su suma.

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
    assert es_numero_perfecto(6) == True, "Error: el test 1 ha fallado."
    assert es_numero_perfecto(28) == True, "Error: considera casos límites en tu lógica."
    assert es_numero_perfecto(10) == False, "Error: el caso base falló."
    assert es_numero_perfecto(1) == False, "Error: el caso 1 debería ser False."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")