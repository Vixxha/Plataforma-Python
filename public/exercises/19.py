# === METADATA ===
# title: Verificador de Números de Armstrong
# description: Crea una función que determine si un número entero positivo es un 'Número de Armstrong'. Un número de n dígitos es un número de Armstrong si la suma de sus dígitos elevados a la potencia n es igual al número mismo.
# difficulty: Intermedio
# expected_output: True para 153 (1^3 + 5^3 + 3^3 = 153), False para 123
# hint: Convierte el número a cadena para iterar sobre sus dígitos y obtener su longitud (n).

# === SOLUTION ===
def es_numero_armstrong(n):
    str_n = str(n)
    potencia = len(str_n)
    suma = sum(int(digito) ** potencia for digito in str_n)
    return suma == n

# === TESTS ===
try:
    assert es_numero_armstrong(153) == True, "Error: el test 1 ha fallado."
    assert es_numero_armstrong(9) == True, "Error: el caso de un solo dígito debe ser True."
    assert es_numero_armstrong(123) == False, "Error: el test 3 ha fallado."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")