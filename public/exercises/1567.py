# === METADATA ===
# title: Validador de Números Primos en Rango
# description: Escribe una función que reciba un número entero positivo y devuelva una lista con todos los números primos que existen desde el 2 hasta ese número (inclusive). Si el número es menor que 2, debe devolver una lista vacía. Debes utilizar iteración y lógica condicional.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Utiliza un bucle para recorrer cada número desde 2 hasta n, y para cada uno, verifica si tiene divisores distintos de 1 y de sí mismo usando otro bucle y condicionales.

# === SOLUTION ===
def primos_hasta_n(n):
    if n < 2:
        return []
    
    primos = []
    for num in range(2, n + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

# === TESTS ===
try:
    assert primos_hasta_n(10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert primos_hasta_n(1) == [], "Error: considera casos límites en tu lógica."
    assert primos_hasta_n(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")