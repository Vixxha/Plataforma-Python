# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y un divisor. La función debe sumar únicamente los números de la lista que sean múltiplos del divisor dado. Si el número es mayor a 100, debe restarse a la suma total en lugar de sumarse.
# difficulty: Intermedio
# expected_output: 10
# hint: Utiliza un bucle for para iterar sobre la lista y una estructura if-elif-else para verificar la divisibilidad y la condición del valor mayor a 100.

# === SOLUTION ===
def procesar_multiplos(numeros, divisor):
    suma = 0
    for num in numeros:
        if num % divisor == 0:
            if num > 100:
                suma -= num
            else:
                suma += num
    return suma

# === TESTS ===
try:
    assert procesar_multiplos([10, 20, 105, 5], 5) == 30, "Error: el test 1 ha fallado."
    assert procesar_multiplos([10, 150, 20], 10) == -120, "Error: considera casos límites en tu lógica."
    assert procesar_multiplos([1, 2, 3], 5) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")