# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y un divisor. La función debe retornar la suma de todos los números en la lista que sean divisibles por el divisor proporcionado, pero solo si el número es mayor que 10. Si un número es mayor a 100, no debe sumarse, sin importar si es divisible o no.
# difficulty: Intermedio
# expected_output: 50 (para input [5, 12, 20, 110, 30] y divisor 2)
# hint: Usa un bucle 'for' para recorrer la lista, y dentro, una estructura condicional 'if' con múltiples condiciones usando 'and'.

# === SOLUTION ===
def sumar_filtrados(lista, divisor):
    suma = 0
    for numero in lista:
        if numero > 10 and numero <= 100 and numero % divisor == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_filtrados([5, 12, 20, 110, 30], 2) == 62, "Error: el test 1 ha fallado."
    assert sumar_filtrados([10, 15, 25, 40], 5) == 80, "Error: considera casos límites en tu lógica."
    assert sumar_filtrados([101, 200, 5], 2) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")