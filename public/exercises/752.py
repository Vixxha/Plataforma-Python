# === METADATA ===
# title: Filtrado de números primos en rango
# description: Implementa una función que reciba un número entero positivo 'n' y retorne una lista con todos los números primos desde 2 hasta 'n' (inclusive), utilizando lógica condicional y estructuras de iteración.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] (para n=10)
# hint: Un número es primo si solo es divisible por 1 y por sí mismo. Puedes iterar desde 2 hasta la raíz cuadrada del número para verificar divisibilidad.

# === SOLUTION ===
def listar_primos(n):
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
    assert listar_primos(10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert listar_primos(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert listar_primos(1) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")