# === METADATA ===
# title: Filtrado de Números Primos
# description: Crea una función que reciba una lista de números enteros y retorne una nueva lista que contenga únicamente los números que sean primos. Un número es primo si es mayor que 1 y solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Recuerda utilizar un bucle para iterar la lista y otro bucle (o una condicional lógica) para verificar si un número tiene divisores distintos a 1 y a sí mismo.

# === SOLUTION ===
def filtrar_primos(lista):
    primos = []
    for numero in lista:
        if numero > 1:
            es_primo = True
            for i in range(2, int(numero**0.5) + 1):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(numero)
    return primos

# === TESTS ===
try:
    assert filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos([11, 13, 17, 19, 20]) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([1, 4, 6, 8, 10]) == [], "Error: el caso base (sin primos) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")