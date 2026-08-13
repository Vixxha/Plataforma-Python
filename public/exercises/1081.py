# === METADATA ===
# title: Verificador de Números Primos
# description: Escribe una función que determine si un número entero positivo es primo o no. Un número primo es aquel que solo es divisible por sí mismo y por 1. Si el número es menor o igual a 1, debe retornar False.
# difficulty: Básico
# expected_output: True para 11, False para 4
# hint: Puedes iterar desde 2 hasta la raíz cuadrada del número para verificar si existe algún divisor exacto.

# === SOLUTION ===
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# === TESTS ===
try:
    assert es_primo(11) == True, "Error: el test 1 ha fallado."
    assert es_primo(4) == False, "Error: considera casos límites en tu lógica."
    assert es_primo(1) == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")