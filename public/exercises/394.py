# === METADATA ===
# title: Verificador de Números Perfectos
# description: Crea una función que determine si un número entero positivo es "perfecto". Un número perfecto es aquel cuya suma de sus divisores propios (excluyendo el número mismo) es igual al propio número.
# difficulty: Intermedio
# expected_output: True para 6, False para 8
# hint: Un número perfecto es igual a la suma de sus divisores, exceptuando él mismo. Itera desde 1 hasta n/2 para encontrar los divisores.

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
    assert es_numero_perfecto(12) == False, "Error: el caso 12 debería ser falso."
    assert es_numero_perfecto(1) == False, "Error: el caso base 1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")