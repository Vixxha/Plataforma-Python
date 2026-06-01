# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y un divisor. La función debe sumar únicamente los números de la lista que sean múltiplos del divisor, ignorando aquellos que sean negativos.
# difficulty: Básico
# expected_output: Para ([1, 2, 3, 4, 5, 6], 2) debería devolver 12 (2 + 4 + 6)
# hint: Utiliza un bucle 'for' para recorrer la lista, un condicional 'if' con el operador módulo (%) para verificar el múltiplo y otro para verificar que el número sea positivo.

# === SOLUTION ===
def sumar_multiplos_positivos(numeros, divisor):
    suma = 0
    for num in numeros:
        if num > 0 and num % divisor == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_positivos([1, 2, 3, 4, 5, 6], 2) == 12, "Error: el test 1 ha fallado."
    assert sumar_multiplos_positivos([-2, 4, 8, 10], 2) == 22, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos_positivos([1, 3, 5, 7], 2) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")