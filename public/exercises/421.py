# === METADATA ===
# title: El Analizador de Números Primos
# description: Crea una función que reciba una lista de números enteros positivos y devuelva una nueva lista que contenga solo aquellos números que sean primos. Un número es primo si es mayor que 1 y no tiene divisores distintos de 1 y de sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para la entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# hint: Utiliza un bucle for para iterar sobre la lista y un bucle anidado (o una condicional avanzada) para verificar si el número tiene algún divisor entre 2 y la raíz cuadrada del propio número.

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
    assert filtrar_primos([11, 13, 17, 19]) == [11, 13, 17, 19], "Error: considera casos con todos primos."
    assert filtrar_primos([1, 4, 6, 8, 9, 10]) == [], "Error: el caso sin primos falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")