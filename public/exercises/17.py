# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es un "número perfecto". Un número es perfecto si la suma de sus divisores propios (excluyendo el número mismo) es igual al número.
# difficulty: Intermedio
# expected_output: True para 6, False para 8
# hint: Itera desde 1 hasta la mitad del número (o hasta la raíz cuadrada) para encontrar los divisores y acumúlalos en una suma.

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
    assert es_numero_perfecto(8) == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")