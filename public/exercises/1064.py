# === METADATA ===
# title: Analizador de Transacciones Numéricas
# description: Escribe una función que reciba una lista de números enteros. Utilizando bucles y lógica condicional, la función debe procesar la lista y retornar una tupla con tres valores: la suma de todos los números pares positivos, la cantidad de números impares negativos y el producto de todos los números que sean múltiplos de 5. Si no hay elementos para el producto, este debe retornar 1.
# difficulty: Intermedio
# expected_output: (30, 2, 50)
# hint: Recuerda inicializar tus acumuladores correctamente (0 para sumas/conteos y 1 para multiplicaciones) y utiliza operadores de módulo (%) y condicionales (if/elif/else) dentro de un bucle for.

# === SOLUTION ===
def analizar_transacciones(numeros):
    suma_pares_positivos = 0
    cantidad_impares_negativos = 0
    producto_multiplos_cinco = 1
    hubo_multiplos_cinco = False

    for n in numeros:
        # Números pares positivos
        if n > 0 and n % 2 == 0:
            suma_pares_positivos += n
        
        # Números impares negativos
        if n < 0 and n % 2 != 0:
            cantidad_impares_negativos += 1
            
        # Múltiplos de 5 (considerando positivos y negativos si aplica, o cualquier entero)
        if n != 0 and n % 5 == 0:
            producto_multiplos_cinco *= n
            hubo_multiplos_cinco = True

    if not hubo_multiplos_cinco:
        producto_multiplos_cinco = 1

    return (suma_pares_positivos, cantidad_impares_negativos, producto_multiplos_cinco)

# === TESTS ===
try:
    assert analizar_transacciones([10, -3, 4, -5, 15, 2, -1]) == (16, 2, -375), "Error: el test 1 ha fallado."
    assert analizar_transacciones([-2, -4, 0, 3]) == (0, 0, 1), "Error: considera casos límites en tu lógica."
    assert analizar_transacciones([5, 10, 2, 4]) == (6, 0, 50), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")