# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5. Si el número es múltiplo de ambos, debe sumarse una sola vez.
# difficulty: Intermedio
# expected_output: 23 (para la lista [1, 3, 5, 10, 15] sería 3 + 5 + 10 + 15 = 33, ajustado a la lógica de sumarlos una vez)
# hint: Utiliza un bucle for para iterar y el operador módulo (%) para verificar las condiciones dentro de un bloque if.

# === SOLUTION ===
def sumar_multiplos(numeros):
    suma_total = 0
    for num in numeros:
        if num % 3 == 0 or num % 5 == 0:
            suma_total += num
    return suma_total

# === TESTS ===
try:
    assert sumar_multiplos([1, 3, 5, 15]) == 23, "Error: el test 1 ha fallado."
    assert sumar_multiplos([10, 20, 30]) == 60, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos([1, 2, 4, 7, 8]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")