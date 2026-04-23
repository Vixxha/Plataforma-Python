# === METADATA ===
# title: Filtrado de Números Primos en Rango
# description: Escribe una función que reciba dos números enteros (inicio y fin) y devuelva una lista con todos los números primos encontrados en ese rango (inclusive). Un número es primo si es mayor que 1 y solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Usa un bucle para iterar sobre el rango y otro bucle anidado (o una lógica condicional) para verificar si el número tiene divisores distintos a 1 y a sí mismo.

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
    assert filtrar_primos(0, 1) == [], "Error: el caso base (sin primos) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")