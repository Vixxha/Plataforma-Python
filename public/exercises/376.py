# === METADATA ===
# title: Filtrado de Números Primos y Suma Acumulada
# description: Crea una función que reciba una lista de números enteros, filtre solo aquellos que son números primos y devuelva la suma total de estos valores. Si no hay números primos en la lista, la función debe retornar 0.
# difficulty: Intermedio
# expected_output: 17 (para la lista [1, 2, 3, 4, 5, 7, 8, 9, 10])
# hint: Un número es primo si es mayor que 1 y solo tiene como divisores el 1 y a sí mismo. Puedes iterar por la lista y usar un bucle anidado o una función auxiliar para verificar la primalidad.

# === SOLUTION ===
def sumar_primos(lista):
    suma = 0
    for num in lista:
        if num > 1:
            es_primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                suma += num
    return suma

# === TESTS ===
try:
    assert sumar_primos([1, 2, 3, 4, 5, 7, 8, 9, 10]) == 17, "Error: el test 1 ha fallado."
    assert sumar_primos([4, 6, 8, 10]) == 0, "Error: considera casos límites donde no hay primos."
    assert sumar_primos([2, 3, 11]) == 16, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")