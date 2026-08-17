# === METADATA ===
# title: Filtrador de Números Primos y Acumulador
# description: Escribe una función que reciba una lista de números enteros y devuelva una nueva lista que contenga únicamente los números primos que sean mayores a 10. Si no hay ninguno que cumpla ambas condiciones, debe devolver una lista vacía.
# difficulty: Intermedio
# expected_output: [11, 13, 17]
# hint: Utiliza un bucle para iterar sobre la lista y un bucle anidado o una función auxiliar para verificar si cada número es primo (divisible solo por 1 y por sí mismo), combinándolo con una condición lógica and.

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
    assert filtrar_primos_mayores_a_diez([4, 7, 11, 13, 20, 25]) == [11, 13], "Error: el test 1 ha fallado."
    assert filtrar_primos_mayores_a_diez([2, 3, 5, 7, 9]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_primos_mayores_a_diez([17, 19, 21, 23, 29]) == [17, 19, 23, 29], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")