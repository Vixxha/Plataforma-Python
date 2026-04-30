# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo es "perfecto". Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al propio número). Ejemplo: 6 es perfecto porque 1 + 2 + 3 = 6.
# difficulty: Intermedio
# expected_output: True para 28, False para 12
# hint: Itera desde 1 hasta la mitad del número (o hasta la raíz cuadrada para mayor eficiencia) para encontrar los divisores.

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
    assert es_numero_perfecto(12) == False, "Error: el caso base falló."
    assert es_numero_perfecto(496) == True, "Error: el test de número perfecto mayor falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")