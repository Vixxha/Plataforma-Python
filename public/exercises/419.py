# === METADATA ===
# title: Filtrado y Suma Condicional
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de todos los números que sean mayores a 10 y, al mismo tiempo, sean pares.
# difficulty: Básico
# expected_output: 36 (para la lista [5, 12, 8, 20, 3, 4])
# hint: Utiliza un bucle 'for' para iterar sobre la lista y una estructura 'if' con un operador lógico 'and' para comprobar ambas condiciones.

# === SOLUTION ===
def sumar_pares_mayores_a_diez(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero > 10 and numero % 2 == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_pares_mayores_a_diez([5, 12, 8, 20, 3, 4]) == 32, "Error: el test 1 ha fallado."
    assert sumar_pares_mayores_a_diez([2, 4, 6, 8]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_pares_mayores_a_diez([10, 12, 14, 11]) == 26, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")