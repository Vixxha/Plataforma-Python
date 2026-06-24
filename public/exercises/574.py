# === METADATA ===
# title: Filtrado y Suma Condicional de Números
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de todos los números positivos que sean menores que 100. Si un número es mayor o igual a 100, ignóralo, y si es negativo, detén la iteración inmediatamente y retorna la suma acumulada hasta ese punto.
# difficulty: Intermedio
# expected_output: Para la lista [10, 50, 150, 5, -2, 20], el resultado debe ser 65.
# hint: Utiliza un bucle 'for' para recorrer los elementos y la palabra reservada 'break' para interrumpir la ejecución al encontrar un número negativo.

# === SOLUTION ===
def sumar_filtrados(lista):
    suma = 0
    for numero in lista:
        if numero < 0:
            break
        if numero < 100:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_filtrados([10, 50, 150, 5, -2, 20]) == 65, "Error: el test 1 ha fallado."
    assert sumar_filtrados([10, 20, 30]) == 60, "Error: considera casos sin números negativos ni mayores a 100."
    assert sumar_filtrados([-5, 10, 20]) == 0, "Error: el caso base falló al empezar con un negativo."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")