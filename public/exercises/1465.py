# === METADATA ===
# title: Filtrar y Sumar Impares
# description: Escribe una función que reciba una lista de números enteros. Debe iterar sobre la lista, filtrar únicamente los números impares, aplicarles el doble a cada uno de esos números impares y devolver la suma total de esos valores resultantes. Si no hay números impares, debe devolver 0.
# difficulty: Intermedio
# expected_output: 36
# hint: Usa un bucle (o comprensión de listas) junto con una estructura condicional (if) y el operador módulo (%) para identificar los números impares.

# === SOLUTION ===
def filtrar_y_sumar_impares(numeros):
    suma = 0
    for num in numeros:
        if num % 2 != 0:
            suma += num * 2
    return suma

# === TESTS ===
try:
    assert filtrar_y_sumar_impares([1, 2, 3, 4, 5]) == 36, "Error: el test 1 ha fallado."
    assert filtrar_y_sumar_impares([2, 4, 6, 8]) == 0, "Error: considera casos límites en tu lógica."
    assert filtrar_y_sumar_impares([-1, -3, 2]) == -8, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")