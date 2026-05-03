# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo el propio número). Ejemplo: 6 = 1 + 2 + 3.
# difficulty: Intermedio
# expected_output: True para 6, False para 8.
# hint: Iterar desde 1 hasta la mitad del número (o hasta la raíz cuadrada para mayor eficiencia) para acumular los divisores.

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
    assert es_numero_perfecto(6) == True, "Error: 6 es un número perfecto."
    assert es_numero_perfecto(28) == True, "Error: 28 es un número perfecto."
    assert es_numero_perfecto(8) == False, "Error: 8 no es un número perfecto."
    assert es_numero_perfecto(1) == False, "Error: 1 no es un número perfecto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")