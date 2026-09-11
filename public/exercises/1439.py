# === METADATA ===
# title: Transponer y Promediar una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros o flotantes, calcule su transpuesta (intercambiar filas por columnas) y devuelva una nueva lista con el promedio de cada columna de la matriz original. El resultado debe redondearse a 2 decimales.
# difficulty: Intermedio
# expected_output: [2.5, 3.5, 4.5]
# hint: Puedes recorrer la matriz por columnas usando los índices o utilizar la función zip() junto con el operador asterisco (*) para transponer las filas y columnas fácilmente.

# === SOLUTION ===
def transponer_y_promediar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    # Transponemos la matriz usando zip
    transpuesta = list(zip(*matriz))
    
    # Calculamos el promedio de cada tupla (columna) y redondeamos a 2 decimales
    promedios = [round(sum(columna) / len(columna), 2) for columna in transpuesta]
    
    return promedios

# === TESTS ===
try:
    assert transponer_y_promediar([[1, 2, 3], [4, 5, 6]]) == [2.5, 3.5, 4.5], "Error: el test 1 ha fallado."
    assert transponer_y_promediar([[10, 20], [30, 40], [50, 60]]) == [30.0, 40.0], "Error: considera casos límites en tu lógica."
    assert transponer_y_promediar([[5]]) == [5.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")