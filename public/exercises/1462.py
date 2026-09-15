# === METADATA ===
# title: Validador y Sumador Condicional de Rango
# description: Escribe una función que reciba una lista de números enteros. La función debe iterar sobre la lista y sumar únicamente aquellos números que sean pares y mayores que cero. Si encuentra el número negativo 999, debe detener la iteración inmediatamente (romper el ciclo). Al finalizar, debe retornar la suma acumulada.
# difficulty: Intermedio
# expected_output: 12
# hint: Utiliza un ciclo `for` o `while` junto con una estructura condicional `if`. Recuerda las palabras clave `break` para detener el ciclo y `continue` o la lógica adecuada para filtrar los números.

# === SOLUTION ===
def sumar_pares_validos(numeros):
    suma = 0
    for num in numeros:
        if num == 999:
            break
        if num > 0 and num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_pares_validos([2, 4, -2, 6, 999, 8]) == 12, "Error: el test 1 ha fallado."
    assert sumar_pares_validos([1, 3, 5, 7]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_pares_validos([10, -5, 4, 0, 2, 999, 8]) == 16, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")