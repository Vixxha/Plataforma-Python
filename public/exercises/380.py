# === METADATA ===
# title: Verificador de Números Perfectos
# description: Implementa una función que determine si un número entero positivo dado es un "número perfecto". Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyéndose a sí mismo).
# difficulty: Intermedio
# expected_output: True para 6, False para 10
# hint: Puedes iterar desde 1 hasta la mitad del número para encontrar sus divisores y sumarlos, o usar la raíz cuadrada para mayor eficiencia.

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
    assert es_numero_perfecto(6) == True, "Error: el test 1 (6) ha fallado."
    assert es_numero_perfecto(28) == True, "Error: el test 2 (28) ha fallado."
    assert es_numero_perfecto(10) == False, "Error: el test 3 (10) ha fallado."
    assert es_numero_perfecto(1) == False, "Error: el caso base (1) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")