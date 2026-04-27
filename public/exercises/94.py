# === METADATA ===
# title: Filtrado de Números Primos en Rango
# description: Escribe una función que reciba un número entero positivo 'n' y retorne una lista con todos los números primos desde 2 hasta 'n' (inclusive). Utiliza bucles para iterar y lógica condicional para verificar la primalidad.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] (para n=10)
# hint: Un número es primo si no es divisible por ningún número entre 2 y su raíz cuadrada. Puedes usar un bucle anidado.

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
    assert listar_primos(2) == [2], "Error: considera casos límites en tu lógica."
    assert listar_primos(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")