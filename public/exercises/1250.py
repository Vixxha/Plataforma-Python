# === METADATA ===
# title: Filtrar y Sumar Pares en Rango
# description: Escribe una función que tome dos números enteros (inicio y fin) que representan un rango inclusivo. La función debe iterar a través de todos los números en ese rango, sumar únicamente aquellos números que sean pares y divisibles por 3 al mismo tiempo, y retornar dicha suma total. Si ningún número cumple la condición, debe retornar 0.
# difficulty: Intermedio
# expected_output: 18 (Para el rango 1 al 10, los pares divisibles por 3 son 6 y 12... espera, del 1 al 10 son 6. Para el rango 1 al 15: 6 + 12 = 18)
# hint: Usa un bucle 'for' con 'range(inicio, fin + 1)' y una estructura condicional 'if' usando el operador módulo '%' para verificar ambas condiciones.

# === SOLUTION ===
def sumar_pares_divisibles_por_tres(inicio, fin):
    suma = 0
    for num in range(inicio, fin + 1):
        if num % 2 == 0 and num % 3 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_pares_divisibles_por_tres(1, 15) == 18, "Error: el test 1 ha fallado."
    assert sumar_pares_divisibles_por_tres(1, 5) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_pares_divisibles_por_tres(6, 6) == 6, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")