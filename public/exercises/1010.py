# === METADATA ===
# title: Validador de Números Primos en Rango
# description: Escribe una función que reciba dos números enteros positivos, inicio y fin, y devuelva una lista con todos los números primos que se encuentran dentro de ese rango (inclusivo). Si el inicio es mayor que el fin o alguno es menor o igual a 0, debe devolver una lista vacía.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Recuerda que un número primo es aquel mayor que 1 que solo es divisible por 1 y por sí mismo. Puedes usar un bucle anidado o una función auxiliar para verificar si cada número en el rango es primo.

# === SOLUTION ===
def primos_en_rango(inicio, fin):
    if inicio <= 0 or fin <= 0 or inicio > fin:
        return []
    
    primos = []
    for num in range(inicio, fin + 1):
        if num < 2:
            continue
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
    assert primos_en_rango(1, 10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert primos_en_rango(10, 20) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert primos_en_rango(15, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")