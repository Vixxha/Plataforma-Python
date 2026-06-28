# === METADATA ===
# title: Filtrado de Números Primos en Rango
# description: Escribe una función que reciba dos números enteros (inicio y fin) y devuelva una lista con todos los números primos encontrados en ese rango, incluyendo ambos extremos.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] (para rango 1 al 10)
# hint: Recuerda que un número es primo si es mayor a 1 y solo es divisible entre 1 y sí mismo. Puedes usar un bucle anidado o una lógica de comprobación de divisores.

# === SOLUTION ===
def filtrar_primos(inicio, fin):
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
    assert filtrar_primos(1, 10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos(10, 20) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert filtrar_primos(1, 2) == [2], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")