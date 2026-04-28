# === METADATA ===
# title: Verificador de Números Primos
# description: Crea una función que determine si un número entero positivo dado es un número primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo.
# difficulty: Básico
# expected_output: True o False
# hint: Recuerda que solo necesitas comprobar divisores hasta la raíz cuadrada del número para optimizar el rendimiento.

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
    assert es_primo(2) == True, "Error: el número 2 debe ser primo."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")