# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es "perfecto". Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al propio número).
# difficulty: Intermedio
# expected_output: True para 6 (1+2+3=6), False para 8 (1+2+4=7)
# hint: Un divisor propio de n es cualquier número d tal que 1 <= d < n y n % d == 0. Considera optimizar el bucle hasta la raíz cuadrada del número.

# === SOLUTION ===
def es_numero_perfecto(n):
    if n <= 1:
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
    assert es_numero_perfecto(6) == True, "Error: el test 1 ha fallado."
    assert es_numero_perfecto(28) == True, "Error: el test 2 ha fallado."
    assert es_numero_perfecto(8) == False, "Error: el test 3 ha fallado."
    assert es_numero_perfecto(1) == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")