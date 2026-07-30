# === METADATA ===
# title: Filtrar y Procesar Números Primos
# description: Escribe una función que reciba una lista de números enteros, filtre únicamente aquellos que sean números primos, y devuelva una lista con el resultado de elevar al cuadrado cada uno de dichos primos. Si la lista no contiene primos, debe devolver una lista vacía.
# difficulty: Intermedio
# expected_output: [4, 9, 25]
# hint: Recuerda que un número primo es mayor que 1 y solo es divisible por 1 y por sí mismo. Puedes usar un bucle anidado o una función auxiliar para verificar la primalidad antes de transformar el número.

# === SOLUTION ===
def procesar_primos(numeros):
    resultado = []
    for n in numeros:
        if n > 1:
            es_primo = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    es_primo = False
                    break
            if es_primo:
                resultado.append(n ** 2)
    return resultado

# === TESTS ===
try:
    assert procesar_primos([1, 2, 3, 4, 5]) == [4, 9, 25], "Error: el test 1 ha fallado."
    assert procesar_primos([10, 11, 12, 13]) == [121, 169], "Error: considera casos límites en tu lógica."
    assert procesar_primos([4, 6, 8, 9]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")