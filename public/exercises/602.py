# === METADATA ===
# title: Filtro y Promedio de Matriz
# description: Crea una función que reciba una matriz de números enteros (lista de listas). La función debe devolver el promedio de todos los elementos que sean mayores que 10. Si no hay elementos mayores a 10, la función debe retornar 0.
# difficulty: Intermedio
# expected_output: 15.0
# hint: Utiliza un bucle anidado para recorrer cada fila y cada columna, acumulando la suma y el conteo de los números que cumplen la condición.

# === SOLUTION ===
def promedio_mayores_a_diez(matriz):
    suma = 0
    contador = 0
    for fila in matriz:
        for elemento in fila:
            if elemento > 10:
                suma += elemento
                contador += 1
    return suma / contador if contador > 0 else 0

# === TESTS ===
try:
    assert promedio_mayores_a_diez([[5, 12], [20, 8]]) == 16.0, "Error: el test 1 ha fallado."
    assert promedio_mayores_a_diez([[1, 2], [3, 4]]) == 0, "Error: considera casos límites en tu lógica."
    assert promedio_mayores_a_diez([[15, 15], [15, 15]]) == 15.0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")