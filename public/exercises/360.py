# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5, pero ignorando cualquier número mayor a 100.
# difficulty: Intermedio
# expected_output: 33 (para la lista [3, 5, 10, 15, 101])
# hint: Utiliza un bucle 'for' para recorrer la lista, un operador de módulo '%' para verificar los múltiplos y una estructura condicional 'if' con operadores lógicos 'or' y 'and'.

# === SOLUTION ===
def sumar_multiplos_especiales(lista):
    suma = 0
    for numero in lista:
        if (numero % 3 == 0 or numero % 5 == 0) and numero <= 100:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_especiales([3, 5, 10, 15, 101]) == 33, "Error: el test 1 ha fallado."
    assert sumar_multiplos_especiales([1, 2, 4, 7, 8]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos_especiales([30, 200, 9]) == 39, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")