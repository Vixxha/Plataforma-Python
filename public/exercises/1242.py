# === METADATA ===
# title: Verificador de Números Armstrong
# description: Escribe una función que determine si un número entero positivo es un número de Armstrong (también conocido como número narcisista). Un número de n dígitos es Armstrong si la suma de cada uno de sus dígitos elevado a la potencia n es igual al propio número. Por ejemplo, 153 es un número Armstrong porque 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
# difficulty: Intermedio
# expected_output: True para 153, False para 123
# hint: Convierte el número a cadena (string) para contar fácilmente cuántos dígitos tiene y para iterar sobre cada uno de ellos.

# === SOLUTION ===
def es_numero_armstrong(n):
    if n < 0:
        return False
    str_n = str(n)
    num_digitos = len(str_n)
    suma = sum(int(digito) ** num_digitos for digito in str_n)
    return suma == n

# === TESTS ===
try:
    assert es_numero_armstrong(153) == True, "Error: el test 1 ha fallado."
    assert es_numero_armstrong(123) == False, "Error: considera casos límites en tu lógica."
    assert es_numero_armstrong(9) == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")