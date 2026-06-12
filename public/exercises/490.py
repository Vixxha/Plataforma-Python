# === METADATA ===
# title: Verificador de Números Perfectos
# description: Crea una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos, excluyendo al propio número.
# difficulty: Intermedio
# expected_output: True para 6, False para 8
# hint: Un divisor propio es cualquier número menor que 'n' que divida a 'n' de forma exacta (residuo 0). Itera desde 1 hasta n/2.

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
    assert es_numero_perfecto(6) == True, "Error: el test 6 ha fallado."
    assert es_numero_perfecto(28) == True, "Error: el test 28 ha fallado."
    assert es_numero_perfecto(8) == False, "Error: el test 8 ha fallado."
    assert es_numero_perfecto(1) == False, "Error: el caso base 1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")