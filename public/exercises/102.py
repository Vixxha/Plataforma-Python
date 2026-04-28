# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5, pero ignorando cualquier número mayor a 100.
# difficulty: Intermedio
# expected_output: 33 (para [3, 5, 10, 11, 15, 105])
# hint: Utiliza un bucle for para iterar sobre la lista y una estructura condicional if con operadores lógicos (or) para verificar las condiciones.

# === SOLUTION ===
def sumar_multiplos_filtrados(numeros):
    suma = 0
    for num in numeros:
        if num <= 100 and (num % 3 == 0 or num % 5 == 0):
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_filtrados([3, 5, 10, 11, 15, 105]) == 33, "Error: el test 1 ha fallado."
    assert sumar_multiplos_filtrados([1, 2, 4, 7]) == 0, "Error: considera casos donde no hay múltiplos."
    assert sumar_multiplos_filtrados([30, 100, 200]) == 130, "Error: el filtro de límites falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")