# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es un "número perfecto". Un número es perfecto si es igual a la suma de sus divisores propios (excluyendo al propio número).
# difficulty: Intermedio
# expected_output: True para 6 (1+2+3=6), False para 8.
# hint: Itera desde 1 hasta la mitad del número (o hasta la raíz cuadrada para mayor eficiencia) para acumular los divisores.

# === SOLUTION ===
def es_numero_perfecto(n):
    if n <= 1:
        return False
    suma_divisores = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

# === TESTS ===
try:
    assert es_numero_perfecto(6) == True, "Error: el test 1 ha fallado."
    assert es_numero_perfecto(28) == True, "Error: considera casos límites en tu lógica."
    assert es_numero_perfecto(12) == False, "Error: el caso base falló."
    assert es_numero_perfecto(1) == False, "Error: los números menores o iguales a 1 no son perfectos."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")