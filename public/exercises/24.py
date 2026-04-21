# === METADATA ===
# title: Filtrado de Números Primos y Suma
# description: Escribe una función que reciba una lista de números enteros y devuelva la suma de todos los números que sean primos. Si el número es menor o igual a 1, no debe ser considerado primo.
# difficulty: Intermedio
# expected_output: 17 (para la lista [1, 2, 3, 4, 5, 7])
# hint: Un número es primo si solo es divisible por 1 y por sí mismo. Puedes usar un bucle 'for' para iterar por la lista y otro bucle (o una condición) para verificar la primalidad de cada elemento.

# === SOLUTION ===
def sumar_primos(lista):
    suma = 0
    for numero in lista:
        if numero > 1:
            es_primo = True
            for i in range(2, int(numero**0.5) + 1):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_primos([1, 2, 3, 4, 5, 7]) == 17, "Error: el test 1 ha fallado."
    assert sumar_primos([10, 11, 12, 13]) == 24, "Error: considera casos límites en tu lógica."
    assert sumar_primos([0, 1, -5, -7]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")