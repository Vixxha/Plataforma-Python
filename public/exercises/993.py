# === METADATA ===
# title: Verificador de Números Primos
# description: Escribe una función que determine si un número entero positivo dado es primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo. La función debe retornar True si es primo y False en caso contrario.
# difficulty: Básico
# expected_output: True para 7, False para 4
# hint: Recuerda que los números menores o iguales a 1 no son primos, y puedes comprobar la divisibilidad iterando desde 2 hasta la raíz cuadrada del número.

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