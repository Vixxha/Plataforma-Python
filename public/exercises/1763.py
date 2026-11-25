# === METADATA ===
# title: Análisis de Matriz de Temperaturas
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros que representan temperaturas diarias en diferentes ciudades. La función debe retornar una nueva lista con el promedio de temperatura de cada ciudad (cada fila), redondeado a 2 decimales.
# difficulty: Intermedio
# expected_output: [22.5, 19.33, 25.0]
# hint: Puedes recorrer cada fila de la matriz, calcular su suma, dividirla entre la cantidad de elementos de la fila y usar round(valor, 2).

# === SOLUTION ===
def promedio_temperaturas(matriz):
    promedios = []
    for fila in matriz:
        if len(fila) == 0:
            promedios.append(0.0)
        else:
            promedio = sum(fila) / len(fila)
            promedios.append(round(promedio, 2))
    return promedios

# === TESTS ===
try:
    assert promedio_temperaturas([[20, 25, 22], [18, 20, 20], [25, 25, 25]]) == [22.33, 19.33, 25.0], "Error: el test 1 ha fallado."
    assert promedio_temperaturas([[10, 20], [30, 40], [15, 25]]) == [15.0, 35.0, 20.0], "Error: considera casos límites en tu lógica."
    assert promedio_temperaturas([[5]]) == [5.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")