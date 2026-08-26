# === METADATA ===
# title: Buscador de Tesoro en Cuadrícula
# description: Dada una matriz (lista de listas) que representa un mapa con diferentes valores numéricos y un número específico que representa un tesoro, escribe una función que devuelva las coordenadas (fila, columna) de la primera aparición del tesoro. Si el tesoro no está en la matriz, debe devolver (-1, -1).
# difficulty: Intermedio
# expected_output: (1, 2)
# hint: Recorre la matriz usando dos bucles anidados (uno para las filas y otro para las columnas) o utilizando índices para verificar cada celda.

# === SOLUTION ===
def encontrar_tesoro(mapa, tesoro):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == tesoro:
                return (i, j)
    return (-1, -1)

# === TESTS ===
try:
    mapa_prueba = [
        [0, 5, 2],
        [9, 1, 7],
        [3, 4, 8]
    ]
    assert encontrar_tesoro(mapa_prueba, 7) == (1, 2), "Error: el test 1 ha fallado."
    assert encontrar_tesoro(mapa_prueba, 9) == (1, 0), "Error: considera casos límites en tu lógica."
    assert encontrar_tesoro(mapa_prueba, 99) == (-1, -1), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")