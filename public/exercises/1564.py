# === METADATA ===
# title: Filtrar y Sumar Números Pares en un Rango
# description: Escribe una función que tome dos números enteros (inicio y fin) que representan un rango inclusivo. La función debe iterar a través de todos los números en ese rango, identificar cuáles son pares y mayores que cero, y devolver la suma total de dichos números. Si el inicio es mayor que el fin, debe retornar 0.
# difficulty: Intermedio
# expected_output: 12
# hint: Utiliza un bucle for con la función range() y una estructura condicional if para verificar si el número es par y positivo antes de sumarlo.

# === SOLUTION ===
def sumar_pares_positivos(inicio, fin):
    suma = 0
    if inicio > fin:
        return 0
    for num in range(inicio, fin + 1):
        if num > 0 and num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_pares_positivos(1, 6) == 12, "Error: el test 1 ha fallado."
    assert sumar_pares_positivos(5, 2) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_pares_positivos(-4, 4) == 6, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")