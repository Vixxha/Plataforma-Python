# === METADATA ===
# title: Validador y Sumador de Números Pares
# description: Escribe una función que reciba una lista de números enteros. La función debe iterar sobre la lista, filtrar únicamente los números que sean pares y positivos, y devolver la suma total de dichos números. Si no hay ningún número que cumpla la condición, debe retornar 0.
# difficulty: Básico
# expected_output: 12
# hint: Puedes usar un bucle `for` para recorrer la lista y una estructura condicional `if` para verificar si un número es positivo (`> 0`) y par (`n % 2 == 0`).

# === SOLUTION ===
def sumar_pares_positivos(numeros):
    suma = 0
    for num in numeros:
        if num > 0 and num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_pares_positivos([1, 2, 3, 4, 5, 6]) == 12, "Error: el test 1 ha fallado."
    assert sumar_pares_positivos([-2, 4, -6, 8]) == 12, "Error: considera casos límites en tu lógica."
    assert sumar_pares_positivos([-1, -3, -5]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")