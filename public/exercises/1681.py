# === METADATA ===
# title: Verificador de Números Primos
# description: Escribe una función que determine si un número entero positivo dado es primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo. La función debe retornar True si es primo y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para 11, False para 4
# hint: Puedes comprobar si el número es divisible por algún entero desde 2 hasta la raíz cuadrada del número. Recuerda que el 1 no es primo.

# === SOLUTION ===
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# === TESTS ===
try:
    assert es_primo(11) == True, "Error: el test 1 ha fallado."
    assert es_primo(4) == False, "Error: considera casos límites en tu lógica."
    assert es_primo(1) == False, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")