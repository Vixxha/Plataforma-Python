# === METADATA ===
# title: Validador de Números Primos en Rango
# description: Escribe una función que reciba dos números enteros (inicio y fin) y utilice bucles y lógica condicional para retornar una lista con todos los números primos que se encuentren dentro de ese rango (inclusive). Si el inicio es mayor que el fin, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Recuerda que un número primo es mayor que 1 y solo es divisible por 1 y por sí mismo. Puedes usar un bucle anidado para verificar los divisores de cada número.

# === SOLUTION ===
def encontrar_primos_en_rango(inicio, fin):
    if inicio > fin:
        return []
    
    primos = []
    for num in range(max(2, inicio), fin + 1):
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
    assert encontrar_primos_en_rango(1, 10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert encontrar_primos_en_rango(10, 2) == [], "Error: considera casos límites en tu lógica."
    assert encontrar_primos_en_rango(11, 19) == [11, 13, 17, 19], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")