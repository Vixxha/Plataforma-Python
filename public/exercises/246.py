# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo dado es un 'número perfecto'. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al propio número).
# difficulty: Intermedio
# expected_output: True para 6, False para 8
# hint: Un número perfecto N tiene divisores que suman N. Por ejemplo, para 6, los divisores son 1, 2 y 3. 1 + 2 + 3 = 6. Puedes iterar hasta la mitad del número para encontrar los divisores.

# === SOLUTION ===
def es_numero_perfecto(n):
    if n <= 1:
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
    assert es_numero_perfecto(1) == False, "Error: el caso del número 1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")