# === METADATA ===
# title: Analizador de Temperaturas Diarias
# description: Escribe una función que reciba una matriz (lista de listas) donde cada fila representa una semana y cada columna un día de la semana con su respectiva temperatura. La función debe retornar una lista con el promedio de temperatura redondeado a 2 decimales de cada semana.
# difficulty: Intermedio
# expected_output: [22.5, 24.1, 19.8]
# hint: Puedes iterar sobre cada fila de la matriz, calcular su suma usando la función sum(), dividirla entre la cantidad de elementos de la fila y usar round(valor, 2) para el redondeo.

# === SOLUTION ===
def calcular_promedios_semanales(matriz):
    promedios = []
    for semana in matriz:
        if len(semana) > 0:
            promedio = round(sum(semana) / len(semana), 2)
            promedios.append(promedio)
        else:
            promedios.append(0.0)
    return promedios

# === TESTS ===
try:
    assert calcular_promedios_semanales([[20, 22, 24, 25, 21, 19, 23], [25, 26, 24, 23, 22, 21, 25]]) == [22.0, 23.57], "Error: el test 1 ha fallado."
    assert calcular_promedios_semanales([[10, 20], [30, 40]]) == [15.0, 35.0], "Error: considera casos límites en tu lógica."
    assert calcular_promedios_semanales([[5, 5, 5]]) == [5.0], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")