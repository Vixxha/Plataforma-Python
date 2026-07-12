# === METADATA ===
# title: Verificador de Números Perfectos
# description: Crea una función que determine si un número entero positivo es "perfecto". Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al mismo número). Ejemplo: 6 es perfecto porque 1 + 2 + 3 = 6.
# difficulty: Intermedio
# expected_output: True o False
# hint: Itera desde 1 hasta la mitad del número para encontrar todos sus divisores y súmalos.

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
    assert es_numero_perfecto(6) == True, "Error: el 6 debería ser perfecto."
    assert es_numero_perfecto(28) == True, "Error: el 28 debería ser perfecto."
    assert es_numero_perfecto(12) == False, "Error: el 12 no debería ser perfecto."
    assert es_numero_perfecto(1) == False, "Error: el 1 no debería ser perfecto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")