# === METADATA ===
# title: Filtrar y Multiplicar Vectores
# description: Escribe una función que reciba una lista de números enteros y un número entero multiplicador. La función debe filtrar los números que sean mayores que el promedio de la lista original y, posteriormente, multiplicar cada uno de esos números filtrados por el valor del multiplicador. Finalmente, debe retornar la nueva lista con los resultados. Si la lista está vacía, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [24, 30]
# hint: Primero calcula el promedio de la lista. Luego, usa comprensión de listas para filtrar y transformar los datos en un solo paso.

# === SOLUTION ===
def filtrar_y_multiplicar(numeros, multiplicador):
    if not numeros:
        return []
    
    promedio = sum(numeros) / len(numeros)
    return [x * multiplicador for x in numeros if x > promedio]

# === TESTS ===
try:
    assert filtrar_y_multiplicar([1, 2, 3, 4, 5], 2) == [8, 10], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar([10, 20, 30], 3) == [90], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar([], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")