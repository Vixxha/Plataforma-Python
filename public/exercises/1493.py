# === METADATA ===
# title: Filtrar y Sumar Impares
# description: Escribe una función que reciba una lista de números enteros, recorra la lista utilizando un bucle, y mediante lógica condicional sume únicamente aquellos números que sean impares y además mayores a 5. La función debe retornar esta suma total.
# difficulty: Básico
# expected_output: 15
# hint: Utiliza un bucle 'for' para recorrer cada número y un condicional 'if' con el operador módulo (%) y el operador mayor que (>) para filtrar correctamente.

# === SOLUTION ===
def filtrar_y_sumar_impares(numeros):
    suma_total = 0
    for num in numeros:
        if num > 5 and num % 2 != 0:
            suma_total += num
    return suma_total

# === TESTS ===
try:
    assert filtrar_y_sumar_impares([1, 3, 5, 7, 9]) == 16, "Error: el test 1 ha fallado."
    assert filtrar_y_sumar_impares([2, 4, 6, 8, 10]) == 0, "Error: considera casos límites en tu lógica."
    assert filtrar_y_sumar_impares([5, 7, 11, 2, 4]) == 18, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")