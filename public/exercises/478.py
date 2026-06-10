# === METADATA ===
# title: El Analizador de Números Primos
# description: Crea una función que reciba una lista de números enteros y devuelva una nueva lista que contenga únicamente los números primos encontrados. Para determinar si un número es primo, utiliza iteraciones y lógica condicional.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Un número es primo si es mayor que 1 y no tiene divisores exactos aparte del 1 y sí mismo. Puedes usar un bucle 'for' para probar divisores desde 2 hasta la raíz cuadrada del número.

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
    assert filtrar_primos([11, 13, 17, 19, 20]) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([0, 1, -5, -10]) == [], "Error: el caso base de números no primos o negativos falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")