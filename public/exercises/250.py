# === METADATA ===
# title: Filtrado de números y cálculo de sumas
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de todos los números pares que sean mayores a 10. Si no hay números que cumplan la condición, la función debe retornar 0.
# difficulty: Básico
# expected_output: Para la lista [5, 12, 8, 20, 7], el resultado debería ser 32 (12 + 20).
# hint: Utiliza un bucle 'for' para iterar sobre la lista y una estructura 'if' con el operador módulo (%) para verificar si el número es par y cumple la condición.

# === SOLUTION ===
def sumar_pares_mayores_a_diez(lista):
    suma = 0
    for numero in lista:
        if numero > 10 and numero % 2 == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_pares_mayores_a_diez([5, 12, 8, 20, 7]) == 32, "Error: el test 1 ha fallado."
    assert sumar_pares_mayores_a_diez([1, 3, 5, 9]) == 0, "Error: considera casos donde no hay números válidos."
    assert sumar_pares_mayores_a_diez([10, 12, 14]) == 26, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")