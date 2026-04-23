# === METADATA ===
# title: Verificador de Números Perfectos
# description: Crea una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo el propio número).
# difficulty: Intermedio
# expected_output: True para 6, False para 8
# hint: Un divisor propio de un número n es cualquier entero d tal que 1 <= d < n y n % d == 0. Considera iterar hasta la mitad del número o hasta su raíz cuadrada para mayor eficiencia.

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
    assert es_numero_perfecto(28) == True, "Error: el 28 es un número perfecto (1+2+4+7+14=28)."
    assert es_numero_perfecto(8) == False, "Error: el 8 no es un número perfecto."
    assert es_numero_perfecto(1) == False, "Error: el 1 no es un número perfecto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")