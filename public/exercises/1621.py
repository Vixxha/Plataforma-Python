# === METADATA ===
# title: Filtrador de Números Primos Acumulativos
# description: Escribe una función que reciba una lista de números enteros y devuelva una nueva lista que contenga únicamente los números primos que sean mayores a 10. Si el número es menor o igual a 10, o no es primo, debe ser ignorado.
# difficulty: Intermedio
# expected_output: [11, 13, 17]
# hint: Utiliza un bucle para iterar sobre la lista y un bucle anidado o una función auxiliar para verificar si cada número es primo, aplicando condiciones para filtrar los valores mayores a 10.

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
    assert filtrar_primos_mayores_a_diez([5, 7, 11, 12, 13, 20, 17]) == [11, 13, 17], "Error: el test 1 ha fallado."
    assert filtrar_primos_mayores_a_diez([2, 3, 5, 7, 9]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_primos_mayores_a_diez([11, 19, 23, 25]) == [11, 19, 23], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")