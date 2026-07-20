# === METADATA ===
# title: Filtrado de Números Primos en un Rango
# description: Escribe una función que reciba dos números enteros (inicio y fin) y retorne una lista con todos los números primos encontrados en ese rango (inclusive). Un número primo es aquel que solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para el rango (1, 10)
# hint: Un número primo debe ser mayor que 1. Puedes iterar desde 2 hasta la raíz cuadrada del número para verificar si tiene divisores.

# === SOLUTION ===
def filtrar_primos(inicio, fin):
    primos = []
    for num in range(max(2, inicio), fin + 1):
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
    assert filtrar_primos(1, 10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos(10, 20) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert filtrar_primos(1, 2) == [2], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")