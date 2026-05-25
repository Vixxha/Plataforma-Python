# === METADATA ===
# title: Verificador de Números Primos
# description: Crea una función que determine si un número entero positivo es un número primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: True para 7, False para 10
# hint: Un número no es primo si tiene algún divisor entre 2 y la raíz cuadrada del número.

# === SOLUTION ===
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# === TESTS ===
try:
    assert es_primo(7) == True, "Error: 7 debería ser primo."
    assert es_primo(10) == False, "Error: 10 no debería ser primo."
    assert es_primo(1) == False, "Error: 1 no es un número primo."
    assert es_primo(2) == True, "Error: 2 es el único primo par."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")