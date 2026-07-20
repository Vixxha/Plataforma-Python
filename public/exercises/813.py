# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5. Si el número es múltiplo de ambos, debe sumarse una sola vez.
# difficulty: Básico
# expected_output: [15, 20] -> 45
# hint: Utiliza el operador módulo (%) para verificar si el residuo de la división es cero y un bucle 'for' junto a una estructura 'if'.

# === SOLUTION ===
def sumar_multiplos(numeros):
    suma = 0
    for num in numeros:
        if num % 3 == 0 or num % 5 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_multiplos([1, 3, 5, 10]) == 18, "Error: el test 1 ha fallado."
    assert sumar_multiplos([15, 20, 30]) == 65, "Error: considera casos donde un número es múltiplo de ambos."
    assert sumar_multiplos([1, 2, 4, 7]) == 0, "Error: el caso base sin múltiplos falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")