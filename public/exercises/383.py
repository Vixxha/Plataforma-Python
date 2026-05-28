# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5, pero ignorando cualquier número mayor a 100.
# difficulty: Intermedio
# expected_output: 23 (Para la lista [3, 5, 10, 101])
# hint: Utiliza un bucle for para iterar sobre la lista y una estructura condicional (if) con operadores lógicos (or, and) para aplicar los filtros.

# === SOLUTION ===
def filtrar_y_sumar(numeros):
    suma = 0
    for num in numeros:
        if num <= 100 and (num % 3 == 0 or num % 5 == 0):
            suma += num
    return suma

# === TESTS ===
try:
    assert filtrar_y_sumar([3, 5, 10, 101]) == 18, "Error: el test 1 ha fallado."
    assert filtrar_y_sumar([15, 20, 105, 3]) == 38, "Error: considera casos límites en tu lógica."
    assert filtrar_y_sumar([1, 2, 4, 7]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")