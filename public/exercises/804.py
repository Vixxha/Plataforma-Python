# === METADATA ===
# title: Filtrado de números y cálculo de promedio
# description: Crea una función que reciba una lista de números enteros, filtre solo aquellos que sean mayores a 10 y menores de 100, y devuelva el promedio de estos. Si no hay números que cumplan la condición, debe retornar 0.
# difficulty: Intermedio
# expected_output: 55.0 (para la entrada [5, 50, 60, 200])
# hint: Utiliza un bucle for para iterar, una variable acumuladora para la suma y un contador para calcular el promedio.

# === SOLUTION ===
def calcular_promedio_filtrado(lista):
    suma = 0
    contador = 0
    for numero in lista:
        if 10 < numero < 100:
            suma += numero
            contador += 1
    
    if contador == 0:
        return 0
    return suma / contador

# === TESTS ===
try:
    assert calcular_promedio_filtrado([5, 50, 60, 200]) == 55.0, "Error: el test 1 ha fallado."
    assert calcular_promedio_filtrado([1, 2, 3]) == 0, "Error: considera casos donde no hay números válidos."
    assert calcular_promedio_filtrado([10, 100, 50]) == 50.0, "Error: el caso con bordes (10 y 100) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")