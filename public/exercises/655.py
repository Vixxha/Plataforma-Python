# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5, pero ignorando cualquier número mayor a 100.
# difficulty: Intermedio
# expected_output: Para la entrada [3, 5, 10, 15, 105, 2], el resultado es 33 (3+5+10+15).
# hint: Utiliza un bucle for para iterar sobre la lista y una estructura condicional if con operadores lógicos (or, and) para validar las condiciones.

# === SOLUTION ===
def sumar_multiplos_filtrados(numeros):
    suma = 0
    for num in numeros:
        if num <= 100 and (num % 3 == 0 or num % 5 == 0):
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_filtrados([3, 5, 10, 15, 105, 2]) == 33, "Error: el test 1 ha fallado."
    assert sumar_multiplos_filtrados([30, 50, 101, 7]) == 80, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos_filtrados([1, 2, 4, 7, 8]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")