# === METADATA ===
# title: Filtrado de Números Primos
# description: Crea una función que reciba una lista de enteros y devuelva una nueva lista que contenga únicamente los números que sean primos.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para la entrada [1, 2, 3, 4, 5, 6, 7, 8, 9]
# hint: Un número primo es aquel mayor a 1 que solo es divisible por sí mismo y por 1. Puedes iterar por cada número y verificar sus divisores usando un bucle anidado.

# === SOLUTION ===
def filtrar_primos(lista):
    primos = []
    for num in lista:
        if num > 1:
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
    assert filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos([11, 13, 17, 19]) == [11, 13, 17, 19], "Error: considera casos con números primos más grandes."
    assert filtrar_primos([0, 1, 4, 6, 8]) == [], "Error: el caso base (sin primos) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")