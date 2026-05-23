# === METADATA ===
# title: Filtrado y Suma Condicional
# description: Crea una función que reciba una lista de números y devuelva la suma de todos los números pares que sean mayores a 10.
# difficulty: Básico
# expected_output: Para [5, 12, 8, 20, 3], debería devolver 32.
# hint: Utiliza un bucle 'for' para iterar sobre la lista y un bloque 'if' con el operador módulo (%) para comprobar la paridad.

# === SOLUTION ===
def sumar_pares_mayores_a_diez(numeros):
    suma = 0
    for num in numeros:
        if num > 10 and num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_pares_mayores_a_diez([5, 12, 8, 20, 3]) == 32, "Error: el test 1 ha fallado."
    assert sumar_pares_mayores_a_diez([2, 4, 6, 8]) == 0, "Error: considera casos donde no hay números mayores a 10."
    assert sumar_pares_mayores_a_diez([10, 14, 22, 30]) == 66, "Error: el caso con múltiples números válidos falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")