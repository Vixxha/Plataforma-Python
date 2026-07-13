# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y un divisor. La función debe retornar la suma de todos los números en la lista que sean divisibles por el divisor, pero solo si el número es mayor a 0. Si el número es negativo o no es divisible, debe ignorarse.
# difficulty: Básico
# expected_output: Para ([10, -5, 20, 7, 30], 5), el resultado es 60
# hint: Utiliza un bucle 'for' para recorrer la lista y una estructura 'if' para comprobar tanto la divisibilidad (operador %) como si el número es positivo.

# === SOLUTION ===
def sumar_multiplos_positivos(lista_numeros, divisor):
    suma = 0
    for num in lista_numeros:
        if num > 0 and num % divisor == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_positivos([10, -5, 20, 7, 30], 5) == 60, "Error: el test 1 ha fallado."
    assert sumar_multiplos_positivos([-10, -20, -30], 5) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos_positivos([3, 6, 9, 12], 3) == 30, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")