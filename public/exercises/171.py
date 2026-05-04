# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos, excluyendo al propio número.
# difficulty: Intermedio
# expected_output: True o False
# hint: Un número es perfecto si la suma de sus divisores desde 1 hasta n-1 es igual al número. Considera optimizar el bucle hasta la raíz cuadrada del número.

# === SOLUTION ===
def es_numero_perfecto(n):
    if n < 2:
        return False
    suma_divisores = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            suma_divisores += i
            if i*i != n:
                suma_divisores += n // i
    return suma_divisores == n

# === TESTS ===
try:
    assert es_numero_perfecto(6) == True, "Error: el 6 es un número perfecto (1+2+3=6)."
    assert es_numero_perfecto(28) == True, "Error: el 28 es un número perfecto (1+2+4+7+14=28)."
    assert es_numero_perfecto(10) == False, "Error: el 10 no es un número perfecto."
    assert es_numero_perfecto(1) == False, "Error: el caso base 1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")