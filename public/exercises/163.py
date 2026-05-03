# === METADATA ===
# title: El Analizador de Números Primos
# description: Crea una función que reciba una lista de números enteros positivos y devuelva una nueva lista que contenga solo los números primos encontrados. Un número primo es aquel mayor a 1 que solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Usa un bucle for para iterar la lista y otro bucle (o una condicional avanzada) para verificar si el número tiene divisores distintos a 1 y a sí mismo.

# === SOLUTION ===
def filtrar_primos(lista_numeros):
    primos = []
    for num in lista_numeros:
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
    assert filtrar_primos([11, 13, 17, 19, 23]) == [11, 13, 17, 19, 23], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([1, 4, 6, 8, 9, 10]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")