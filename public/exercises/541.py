# === METADATA ===
# title: Filtrado de números primos en rango
# description: Implementa una función que reciba un número entero positivo 'n' y retorne una lista con todos los números primos desde 2 hasta 'n' (inclusive). Utiliza bucles anidados y lógica condicional para determinar la primalidad.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para n=10
# hint: Recuerda que un número primo solo es divisible por 1 y por sí mismo. Puedes usar un bucle 'for' para iterar hasta n y otro para comprobar divisores hasta la raíz cuadrada del número.

# === SOLUTION ===
def filtrar_primos(n):
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
    assert filtrar_primos(10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert filtrar_primos(2) == [2], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")