# === METADATA ===
# title: Filtrado de Números Primos
# description: Implementa una función que reciba una lista de enteros y devuelva una nueva lista que contenga solo aquellos números que sean primos. Un número es primo si es mayor a 1 y solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Utiliza un bucle for para iterar sobre la lista y un bucle anidado o una validación condicional para comprobar si el número es divisible por algún valor entre 2 y su raíz cuadrada.

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
    assert filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos([11, 13, 17, 19]) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([0, 1, 4, 6, 8, 9]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")