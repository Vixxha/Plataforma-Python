# === METADATA ===
# title: Filtrado de Números Primos
# description: Crea una función que reciba una lista de números enteros y devuelva una nueva lista que contenga solo aquellos números que sean primos. Un número es primo si solo es divisible por 1 y por sí mismo, y es mayor que 1.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para la entrada [1, 2, 3, 4, 5, 6, 7, 8, 9]
# hint: Utiliza un bucle for para iterar sobre la lista y un bucle anidado o un rango para verificar divisores desde 2 hasta la raíz cuadrada del número.

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
    assert filtrar_primos([11, 13, 17, 19]) == [11, 13, 17, 19], "Error: considera casos con números primos mayores."
    assert filtrar_primos([0, 1, 4, 6, 8]) == [], "Error: el caso base falló (ningún primo)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")