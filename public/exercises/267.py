# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3, pero que no sean múltiplos de 5.
# difficulty: Básico
# expected_output: [3, 6, 9, 12, 18] -> 48
# hint: Utiliza un bucle for para recorrer la lista, un operador módulo (%) para verificar las condiciones y una variable acumuladora para el resultado.

# === SOLUTION ===
def sumar_filtrados(numeros):
    suma = 0
    for num in numeros:
        if num % 3 == 0 and num % 5 != 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_filtrados([1, 3, 5, 6, 9, 10, 15, 18]) == 36, "Error: el test 1 ha fallado."
    assert sumar_filtrados([30, 45, 60]) == 0, "Error: considera casos donde todos son múltiplos de 5."
    assert sumar_filtrados([]) == 0, "Error: el caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")