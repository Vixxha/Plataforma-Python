# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva su transpuesta (intercambiar filas por columnas), pero donde cada elemento de la matriz resultante sea elevado al cuadrado si es un número par, o se mantenga igual si es impar.
# difficulty: Intermedio
# expected_output: [[1, 9], [4, 25]] para la entrada [[1, 2], [3, 5]] -> Transpuesta: [[1, 3], [2, 5]] -> Procesada: [[1, 3], [4, 5]] ... espera, 2 al cuadrado es 4, 3 queda igual, 5 queda igual, 1 queda igual.
# hint: Puedes primero calcular la transpuesta recorriendo las columnas y luego aplicar la condición a cada elemento. Recuerda que la transpuesta de una matriz intercambia las dimensiones (filas por columnas).

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear la matriz transpuesta
    transpuesta = [[matriz[r][c] for r in range(filas)] for c in range(columnas)]
    
    # Aplicar la condición: elevar al cuadrado si es par, dejar igual si es impar
    resultado = []
    for fila in transpuesta:
        nueva_fila = []
        for val in fila:
            if val % 2 == 0:
                nueva_fila.append(val ** 2)
            else:
                nueva_fila.append(val)
        resultado.append(nueva_fila)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2], [3, 4]]) == [[1, 3], [4, 16]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[5, 6, 7], [8, 9, 10]]) == [[5, 64], [36, 9], [7, 100]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[2]]) == [[4]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")