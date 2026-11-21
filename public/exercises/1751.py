# === METADATA ===
# title: Verificador de Números Primos
# description: Escribe una función que determine si un número entero dado es primo. Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores positivos distintos: él mismo y el 1. La función debe retornar True si es primo y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para 7, False para 4, True para 2
# hint: Recuerda que solo necesitas comprobar si el número es divisible por algún entero desde 2 hasta la raíz cuadrada del número.

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
    assert es_primo(2) == True, "Error: el caso base falló."
    assert es_primo(1) == False, "Error: el 1 no es un número primo."
    assert es_primo(11) == True, "Error: el 11 es primo."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")