# === METADATA ===
# title: Verificador de Números Perfectos
# description: Crea una función que determine si un número entero positivo es un número perfecto. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyéndose a sí mismo).
# difficulty: Intermedio
# expected_output: True para 6, False para 10
# hint: Un divisor propio de 'n' es cualquier número desde 1 hasta n/2 que divida a 'n' sin dejar residuo.

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
    assert es_numero_perfecto(6) == True, "Error: el test 1 ha fallado."
    assert es_numero_perfecto(28) == True, "Error: considera casos límites en tu lógica."
    assert es_numero_perfecto(10) == False, "Error: el caso base falló."
    assert es_numero_perfecto(1) == False, "Error: el 1 no debe ser considerado perfecto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")