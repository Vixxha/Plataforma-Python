# === METADATA ===
# title: El Analizador de Números Primos
# description: Crea una función que reciba una lista de números enteros positivos y retorne una nueva lista que contenga únicamente los números que sean primos. Un número es primo si es mayor que 1 y solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Para verificar si un número 'n' es primo, intenta dividirlo por todos los números desde 2 hasta n-1; si alguno tiene resto cero, no es primo.

# === SOLUTION ===
def filtrar_primos(lista_numeros):
    primos = []
    for num in lista_numeros:
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
    assert filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos([11, 13, 17, 19]) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([1, 4, 6, 8, 9]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")