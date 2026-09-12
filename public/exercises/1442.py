# === METADATA ===
# title: Filtrar y Sumar Pares en Rango
# description: Escribe una función que reciba dos números enteros (inicio y fin) que representan un rango inclusivo. La función debe iterar a través de todos los números en ese rango, sumar únicamente aquellos números que sean pares y cuyo valor sea divisible por 3, y retornar dicha suma total.
# difficulty: Intermedio
# expected_output: 18 (para el rango de 1 a 10, los pares divisibles por 3 son 6 y 12... espera: de 1 a 10 los pares son 2,4,6,8,10. Los divisibles por 3 son 6. Si el rango es 1 a 12, los pares divisibles por 3 son 6 y 12, suma = 18).
# hint: Utiliza un bucle for con la función range(), y combina operadores aritméticos y condicionales (if) usando el operador módulo (%).

# === SOLUTION ===
def sumar_pares_divisibles_por_tres(inicio, fin):
    suma_total = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0 and numero % 3 == 0:
            suma_total += numero
    return suma_total

# === TESTS ===
try:
    assert sumar_pares_divisibles_por_tres(1, 12) == 18, "Error: el test 1 ha fallado."
    assert sumar_pares_divisibles_por_tres(1, 5) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_pares_divisibles_por_tres(6, 6) == 6, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")