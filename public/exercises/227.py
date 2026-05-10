# === METADATA ===
# title: El Analizador de Números Primos y Divisores
# description: Crea una función que reciba una lista de números enteros y devuelva una nueva lista que contenga solo aquellos números que son mayores a 10 y que sean números primos.
# difficulty: Intermedio
# expected_output: [11, 13, 17]
# hint: Recuerda que un número primo es aquel que solo es divisible por 1 y por sí mismo. Puedes iterar por la lista y para cada número usar un bucle anidado para verificar sus divisores.

# === SOLUTION ===
def filtrar_primos_mayores_a_diez(numeros):
    resultado = []
    for num in numeros:
        if num > 10:
            es_primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                resultado.append(num)
    return resultado

# === TESTS ===
try:
    assert filtrar_primos_mayores_a_diez([2, 5, 11, 13, 15, 17, 20]) == [11, 13, 17], "Error: el test 1 ha fallado."
    assert filtrar_primos_mayores_a_diez([1, 2, 3, 4, 5]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_primos_mayores_a_diez([23, 25, 29]) == [23, 29], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")