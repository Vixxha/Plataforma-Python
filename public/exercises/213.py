# === METADATA ===
# title: Filtrado y Normalización de Matriz
# description: Crea una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde todos los valores negativos hayan sido reemplazados por 0 y los valores superiores a 100 por 100.
# difficulty: Intermedio
# expected_output: [[0, 50, 100], [20, 0, 100]]
# hint: Puedes recorrer la matriz usando dos bucles anidados o una comprensión de listas anidada para generar la nueva estructura.

# === SOLUTION ===
def normalizar_matriz(matriz):
    resultado = []
    for fila in matriz:
        nueva_fila = []
        for valor in fila:
            if valor < 0:
                nueva_fila.append(0)
            elif valor > 100:
                nueva_fila.append(100)
            else:
                nueva_fila.append(valor)
        resultado.append(nueva_fila)
    return resultado

# === TESTS ===
try:
    assert normalizar_matriz([[-10, 50, 150], [20, -5, 300]]) == [[0, 50, 100], [20, 0, 100]], "Error: el test 1 ha fallado."
    assert normalizar_matriz([[0, 0], [100, 100]]) == [[0, 0], [100, 100]], "Error: considera casos límites en tu lógica."
    assert normalizar_matriz([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")