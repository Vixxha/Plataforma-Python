# === METADATA ===
# title: Analizador de Secuencia Numérica
# description: Escribe una función que reciba una lista de números enteros. Debe iterar sobre la lista y retornar una tupla con dos valores: la suma de todos los números pares y la cantidad de números impares encontrados que sean mayores a 5.
# difficulty: Intermedio
# expected_output: (20, 2)
# hint: Utiliza un bucle para recorrer la lista, condicionales (if) para verificar si un número es par (n % 2 == 0) y si es impar mayor que 5.

# === SOLUTION ===
def analizar_secuencia(numeros):
    suma_pares = 0
    contador_impares_mayores_a_cinco = 0
    
    for num in numeros:
        if num % 2 == 0:
            suma_pares += num
        else:
            if num > 5:
                contador_impares_mayores_a_cinco += 1
                
    return (suma_pares, contador_impares_mayores_a_cinco)

# === TESTS ===
try:
    assert analizar_secuencia([1, 2, 3, 4, 6, 7, 9]) == (12, 2), "Error: el test 1 ha fallado."
    assert analizar_secuencia([10, 11, 12, 3]) == (22, 0), "Error: considera casos límites en tu lógica."
    assert analizar_secuencia([5, 15, 25]) == (0, 2), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")