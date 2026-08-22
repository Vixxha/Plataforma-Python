# === METADATA ===
# title: Filtrar y Sumar Impares Válidos
# description: Escribe una función que reciba una lista de números enteros. La función debe iterar sobre la lista, ignorar los números menores o iguales a 0, y sumar únicamente aquellos números que sean impares. Al finalizar, debe retornar el valor total de dicha suma.
# difficulty: Básico
# expected_output: 16
# hint: Utiliza un bucle for para recorrer los elementos, una condición if para verificar que el número sea mayor que cero y otra para comprobar si es impar (usando el operador módulo `%`).

# === SOLUTION ===
def sumar_impares_validos(numeros):
    suma = 0
    for num in numeros:
        if num > 0 and num % 2 != 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_impares_validos([1, 2, 3, 4, 5, -3]) == 9, "Error: el test 1 ha fallado."
    assert sumar_impares_validos([-5, -1, 0, 2, 4]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_impares_validos([7, 3, 6, 9, -2]) == 19, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")