# === METADATA ===
# title: Verificador de Números Perfectos
# description: Crea una función que determine si un número entero positivo es un 'número perfecto'. Un número perfecto es aquel cuya suma de sus divisores propios (excluyéndose a sí mismo) es igual al propio número. Por ejemplo, 6 es perfecto porque 1 + 2 + 3 = 6.
# difficulty: Intermedio
# expected_output: True o False
# hint: Iterar desde 1 hasta la mitad del número (o hasta la raíz cuadrada para mayor eficiencia) para acumular la suma de los divisores.

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
    assert es_numero_perfecto(28) == True, "Error: 28 debe ser perfecto (1+2+4+7+14=28)."
    assert es_numero_perfecto(12) == False, "Error: 12 no es perfecto."
    assert es_numero_perfecto(1) == False, "Error: el caso base 1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")