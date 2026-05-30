# === METADATA ===
# title: Filtrado de Números Primos en Rango
# description: Escribe una función que reciba dos números enteros (inicio y fin) y retorne una lista con todos los números primos encontrados en ese rango (inclusive). Un número es primo si solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para el rango (1, 10)
# hint: Un número menor a 2 no es primo. Utiliza un bucle for para iterar el rango y un bucle anidado o lógica condicional para verificar divisibilidad hasta la raíz cuadrada del número.

# === SOLUTION ===
def obtener_primos(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if num > 1:
            es_primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(num)
    return primos

# === TESTS ===
try:
    assert obtener_primos(1, 10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert obtener_primos(10, 20) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert obtener_primos(1, 2) == [2], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")