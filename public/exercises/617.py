# === METADATA ===
# title: Filtrado de números primos en rango
# description: Crea una función que reciba una lista de números enteros y devuelva una nueva lista que contenga solo aquellos números que sean primos. Un número es primo si es mayor que 1 y no tiene divisores distintos a 1 y a sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7, 11] para la entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# hint: Usa un bucle 'for' para iterar la lista y una lógica condicional con un segundo bucle o un rango para verificar si el número tiene divisores.

# === SOLUTION ===
def filtrar_primos(numeros):
    primos = []
    for n in numeros:
        if n < 2:
            continue
        es_primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
    return primos

# === TESTS ===
try:
    assert filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [2, 3, 5, 7, 11], "Error: el test 1 ha fallado."
    assert filtrar_primos([10, 12, 14, 15]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([2, 13, 17, 19]) == [2, 13, 17, 19], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")