# === METADATA ===
# title: Filtrar y Sumar Pares en Rango
# description: Escribe una función que reciba dos números enteros (inicio y fin) que representan un rango inclusivo. La función debe iterar a través de todos los números en ese rango, identificar cuáles son pares y devolver la suma total de dichos números pares. Si el inicio es mayor que el fin, debe retornar 0.
# difficulty: Intermedio
# expected_output: 30
# hint: Utiliza un bucle for junto con la función range() y una estructura condicional if para verificar si cada número es divisible por 2 (num % 2 == 0).

# === SOLUTION ===
def sumar_pares_en_rango(inicio, fin):
    suma = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_pares_en_rango(1, 10) == 30, "Error: el test 1 ha fallado."
    assert sumar_pares_en_rango(5, 5) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_pares_en_rango(10, 1) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")