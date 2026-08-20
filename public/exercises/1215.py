# === METADATA ===
# title: Validador y Sumador de Números Pares
# description: Escribe una función que reciba una lista de números enteros. La función debe iterar sobre la lista, filtrar únicamente los números pares que sean mayores a 10 y retornar la suma total de dichos números. Si no hay ningún número que cumpla con la condición, debe retornar 0.
# difficulty: Intermedio
# expected_output: 30
# hint: Usa un bucle 'for' para recorrer la lista y una estructura condicional 'if' para verificar si el número es par (n % 2 == 0) y mayor que 10.

# === SOLUTION ===
def suma_pares_mayores_a_diez(numeros):
    suma = 0
    for num in numeros:
        if num > 10 and num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert suma_pares_mayores_a_diez([4, 12, 15, 18, 7]) == 30, "Error: el test 1 ha fallado."
    assert suma_pares_mayores_a_diez([2, 4, 6, 8, 10]) == 0, "Error: considera casos límites en tu lógica."
    assert suma_pares_mayores_a_diez([20, 22, 5, 3]) == 42, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")