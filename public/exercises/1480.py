# === METADATA ===
# title: Verificador de Números Armstrong
# description: Escribe una función que determine si un número entero positivo es un número de Armstrong (también conocido como número narcisista). Un número de n dígitos es Armstrong si la suma de cada uno de sus dígitos elevado a la potencia n es igual al propio número.
# difficulty: Intermedio
# expected_output: True para 153, False para 123
# hint: Convierte el número a string o usa operaciones matemáticas para extraer cada dígito y cuenta la cantidad total de dígitos para usarla como exponente.

# === SOLUTION ===
def es_numero_armstrong(numero):
    if numero < 0:
        return False
    digitos = str(numero)
    n = len(digitos)
    suma = sum(int(d) ** n for d in digitos)
    return suma == numero

# === TESTS ===
try:
    assert es_numero_armstrong(153) == True, "Error: el test 1 ha fallado."
    assert es_numero_armstrong(123) == False, "Error: considera casos límites en tu lógica."
    assert es_numero_armstrong(9474) == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")