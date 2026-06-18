# === METADATA ===
# title: Verificador de Números Perfectos
# description: Escribe una función que determine si un número entero positivo es "perfecto". Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al propio número).
# difficulty: Intermedio
# expected_output: True para 6, False para 8
# hint: Un número perfecto es igual a la suma de sus divisores. Iterar hasta la mitad del número (o hasta la raíz cuadrada) puede optimizar tu algoritmo.

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
    assert es_numero_perfecto(6) == True, "Error: el 6 es un número perfecto."
    assert es_numero_perfecto(28) == True, "Error: el 28 es un número perfecto."
    assert es_numero_perfecto(8) == False, "Error: el 8 no es un número perfecto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")