# === METADATA ===
# title: Verificador de Números Primos y Divisores
# description: Escribe una función que reciba un número entero positivo y determine si es un número primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo (mayores que 1). La función debe retornar True si es primo y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para 7, False para 4, False para 1
# hint: Puedes iterar desde 2 hasta la raíz cuadrada del número para comprobar si alguno de esos valores lo divide exactamente.

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
    assert es_primo(11) == True, "Error: el test de número primo mayor falló."
    assert es_primo(9) == False, "Error: el test de número compuesto falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")