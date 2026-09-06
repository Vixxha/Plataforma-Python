# === METADATA ===
# title: Filtrar y Sumar Impares
# description: Escribe una función que reciba una lista de números enteros, recorra la lista utilizando un bucle, y mediante lógica condicional sume únicamente aquellos números que sean impares y mayores a cero. Si no hay números que cumplan la condición, debe retornar 0.
# difficulty: Básico
# expected_output: 9
# hint: Utiliza un bucle 'for' para recorrer los elementos y el operador módulo '%' junto con un condicional 'if' para verificar si el número es impar y positivo.

# === SOLUTION ===
def sumar_impares_positivos(numeros):
    suma = 0
    for num in numeros:
        if num > 0 and num % 2 != 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_impares_positivos([1, 2, 3, 4, 5]) == 9, "Error: el test 1 ha fallado."
    assert sumar_impares_positivos([-1, -3, 0, 2, 4]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_impares_positivos([7, -5, 3, 2, 9]) == 19, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")