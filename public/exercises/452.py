# === METADATA ===
# title: El Analizador de Números Primos
# description: Crea una función que reciba un número entero positivo y devuelva una lista con todos los números primos encontrados desde el 2 hasta dicho número (inclusive). Si el número es menor que 2, devuelve una lista vacía.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Un número primo solo es divisible por 1 y por sí mismo. Puedes usar un bucle anidado para verificar si cada número tiene divisores entre 2 y su raíz cuadrada.

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
    assert obtener_primos(1) == [], "Error: considera casos límites en tu lógica."
    assert obtener_primos(2) == [2], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")