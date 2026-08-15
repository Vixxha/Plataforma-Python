# === METADATA ===
# title: Verificador de Números Primos y Divisores
# description: Escribe una función que determine si un número entero positivo es primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo (considera que los números menores o iguales a 1 no son primos).
# difficulty: Básico
# expected_output: True para 7, False para 4
# hint: Puedes comprobar si el número tiene algún divisor desde el 2 hasta la raíz cuadrada del número. Si encuentras alguno, no es primo.

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
    assert es_primo(7) == True, "Error: el test 1 ha fallado."
    assert es_primo(4) == False, "Error: considera casos límites en tu lógica."
    assert es_primo(1) == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")