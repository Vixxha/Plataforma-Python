# === METADATA ===
# title: El Analizador de Números Primos
# description: Implementa una función que reciba una lista de números enteros y devuelva una nueva lista que contenga únicamente los números que sean primos. Si un número es menor o igual a 1, no debe incluirse.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Recuerda que un número primo es aquel que solo es divisible por 1 y por sí mismo. Puedes usar un bucle `for` para iterar sobre la lista y otro bucle `for` anidado para verificar la divisibilidad hasta la raíz cuadrada del número.

# === SOLUTION ===
def filtrar_primos(lista):
    primos = []
    for numero in lista:
        if numero < 2:
            continue
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(numero)
    return primos

# === TESTS ===
try:
    assert filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos([11, 13, 17, 19]) == [11, 13, 17, 19], "Error: considera casos con todos los elementos primos."
    assert filtrar_primos([0, 1, 4, 6, 8]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")