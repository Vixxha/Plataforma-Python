# === METADATA ===
# title: Filtrar y Sumar Divisores
# description: Escribe una función que reciba una lista de números enteros y un número divisor. La función debe recorrer la lista y sumar únicamente aquellos números que sean divisibles por el divisor dado y que, además, sean mayores que cero.
# difficulty: Intermedio
# expected_output: 15
# hint: Utiliza un bucle for para recorrer la lista, una estructura condicional (if) para verificar si el número es mayor que cero y si es divisible usando el operador módulo (%), y acumula el resultado.

# === SOLUTION ===
def sumar_divisibles(numeros, divisor):
    suma = 0
    for num in numeros:
        if num > 0 and num % divisor == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_divisibles([10, -5, 3, 6, 9, 2], 3) == 18, "Error: el test 1 ha fallado."
    assert sumar_divisibles([-3, -6, 0, 4], 2) == 4, "Error: considera casos límites en tu lógica."
    assert sumar_divisibles([1, 2, 3, 4, 5], 10) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")