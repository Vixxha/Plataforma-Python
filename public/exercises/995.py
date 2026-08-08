# === METADATA ===
# title: El Analizador de Secuencias Numéricas
# description: Escribe una función que reciba una lista de números enteros y procese cada elemento utilizando bucles y condiciones. La función debe ignorar los números menores o iguales a 0, sumar los números pares encontrados y contar cuántos números impares mayores a 10 hay. Finalmente, debe devolver una tupla con ambos resultados: (suma_pares, contador_impares_mayores_a_10).
# difficulty: Intermedio
# expected_output: (30, 2)
# hint: Utiliza un bucle for para recorrer la lista, estructuras condicionales (if, elif, else) para filtrar según las reglas, y operadores aritméticos y de comparación.

# === SOLUTION ===
def analizar_secuencia(numeros):
    suma_pares = 0
    contador_impares_mayores_10 = 0
    
    for num in numeros:
        if num <= 0:
            continue
        
        if num % 2 == 0:
            suma_pares += num
        else:
            if num > 10:
                contador_impares_mayores_10 += 1
                
    return (suma_pares, contador_impares_mayores_10)

# === TESTS ===
try:
    assert analizar_secuencia([4, 11, -5, 10, 15, 2, 0]) == (16, 2), "Error: el test 1 ha fallado."
    assert analizar_secuencia([-2, -8, 0]) == (0, 0), "Error: considera casos límites en tu lógica."
    assert analizar_secuencia([12, 13, 14, 5]) == (26, 0), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")