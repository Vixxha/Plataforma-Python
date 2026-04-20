# === METADATA ===
# title: Verificador de Números Primos
# description: Crea una función que determine si un número entero positivo es un número primo. Un número primo es aquel que solo es divisible por sí mismo y por 1. El programa debe retornar True si es primo y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para 7, False para 10
# hint: Un número no es primo si tiene algún divisor entre 2 y la raíz cuadrada del propio número.

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
    assert es_primo(7) == True, "Error: el test 1 ha fallado."
    assert es_primo(10) == False, "Error: considera casos límites en tu lógica."
    assert es_primo(1) == False, "Error: el caso base falló."
    assert es_primo(2) == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")