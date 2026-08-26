# === METADATA ===
# title: Verificador de Números Perfectos
# description: Escribe una función que determine si un número entero positivo es un número perfecto. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al propio número).
# difficulty: Intermedio
# expected_output: True para 6 (1+2+3=6), False para 10
# hint: Utiliza un bucle para encontrar todos los números menores que n que dividan exactamente a n, y acumula su suma.

# === SOLUTION ===
def es_numero_perfecto(n):
    if n <= 1:
        return False
    suma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return suma_divisores == n

# === TESTS ===
try:
    assert es_numero_perfecto(6) == True, "Error: el test 1 ha fallado."
    assert es_numero_perfecto(28) == True, "Error: considera casos límites en tu lógica."
    assert es_numero_perfecto(10) == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")