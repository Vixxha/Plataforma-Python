# === METADATA ===
# title: Filtrado de Números Primos en Rango
# description: Escribe una función que reciba un número entero positivo 'n' y devuelva una lista con todos los números primos desde 2 hasta 'n' (inclusive). Un número es primo si solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para n=10
# hint: Utiliza un bucle anidado: el externo para iterar hasta 'n' y el interno para verificar si existe algún divisor entre 2 y la raíz cuadrada del número actual.

# === SOLUTION ===
def obtener_primos(n):
    primos = []
    for num in range(2, n + 1):
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

# === TESTS ===
try:
    assert obtener_primos(10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert obtener_primos(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert obtener_primos(2) == [2], "Error: el caso base falló."
    assert obtener_primos(1) == [], "Error: el caso para n=1 debería devolver una lista vacía."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")