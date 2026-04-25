# === METADATA ===
# title: El Analizador de Números Primos
# description: Implementa una función que reciba una lista de números enteros y devuelva una nueva lista que contenga únicamente los números que sean primos. Un número es primo si es mayor que 1 y solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7, 11] para la entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# hint: Utiliza un bucle para iterar la lista y un segundo bucle (o una condición) para verificar si el número tiene algún divisor entre 2 y la raíz cuadrada del mismo.

# === SOLUTION ===
def filtrar_primos(lista):
    primos = []
    for num in lista:
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
    assert filtrar_primos([1, 2, 3, 4, 5]) == [2, 3, 5], "Error: el test 1 ha fallado."
    assert filtrar_primos([10, 15, 20]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([2, 7, 13, 17]) == [2, 7, 13, 17], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")