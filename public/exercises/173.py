# === METADATA ===
# title: El Analizador de Números Primos
# description: Crea una función que reciba un número entero positivo y devuelva una lista con todos los números primos encontrados desde el 2 hasta dicho número (incluyéndolo).
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para el input 10
# hint: Recuerda que un número primo solo es divisible por 1 y por sí mismo. Puedes usar un bucle anidado o una variable booleana para verificar la divisibilidad.

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