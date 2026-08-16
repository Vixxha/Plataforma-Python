# === METADATA ===
# title: Validador de Números Primos en Rango
# description: Escribe una función que reciba dos números enteros positivos, 'inicio' y 'fin', y devuelva una lista con todos los números primos que se encuentran dentro de ese rango (inclusivo). Si el inicio es mayor que el fin o algún número es menor o igual a 1, debe devolver una lista vacía.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Utiliza un bucle para recorrer el rango y otro bucle (o una función auxiliar) para verificar si cada número es divisible únicamente por 1 y por sí mismo. Recuerda manejar las condiciones de validación iniciales.

# === SOLUTION ===
def primos_en_rango(inicio, fin):
    if inicio > fin or fin <= 1:
        return []
    
    primos = []
    for num in range(max(2, inicio), fin + 1):
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
    assert primos_en_rango(1, 10) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert primos_en_rango(10, 1) == [], "Error: considera casos límites en tu lógica."
    assert primos_en_rango(11, 20) == [11, 13, 17, 19], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")