# === METADATA ===
# title: Verificador de Números Perfectos
# description: Crea una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos, excluyéndose a sí mismo.
# difficulty: Intermedio
# expected_output: True para 6, False para 8
# hint: Un divisor propio es cualquier número menor que n que divida a n sin dejar residuo. Puedes iterar desde 1 hasta n/2.

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
    assert es_numero_perfecto(28) == True, "Error: el 28 debería ser perfecto."
    assert es_numero_perfecto(8) == False, "Error: el 8 no es un número perfecto."
    assert es_numero_perfecto(1) == False, "Error: el 1 no cumple la definición."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")