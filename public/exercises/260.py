# === METADATA ===
# title: Analizador de Números Primos en Rango
# description: Escribe una función que reciba un número entero positivo 'n' y retorne una lista con todos los números primos encontrados entre 1 y 'n' (inclusive). Un número primo es aquel mayor a 1 que solo es divisible por sí mismo y por 1.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para el input 10
# hint: Utiliza un bucle for para iterar hasta 'n' y un bucle anidado o una lógica condicional para verificar si cada número tiene divisores distintos a 1 y a sí mismo.

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
    assert obtener_primos(1) == [], "Error: el caso base (n < 2) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")