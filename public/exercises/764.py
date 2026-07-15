# === METADATA ===
# title: Filtrado de Números Primos
# description: Crea una función que reciba una lista de números enteros y retorne una nueva lista que contenga únicamente los números que sean primos. Un número es primo si solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Recuerda que los números menores o iguales a 1 no son primos. Puedes usar un bucle 'for' para iterar y un 'if' con un contador o una bandera para verificar divisibilidad.

# === SOLUTION ===
def filtrar_primos(numeros):
    primos = []
    for num in numeros:
        if num < 2:
            continue
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
    assert filtrar_primos([1, 2, 3, 4, 5, 6]) == [2, 3, 5], "Error: el test 1 ha fallado."
    assert filtrar_primos([10, 11, 13, 17, 20]) == [11, 13, 17], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([0, 1]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")