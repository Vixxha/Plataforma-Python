# === METADATA ===
# title: Filtrar y sumar números pares con límite
# description: Escribe una función que reciba una lista de enteros y un número límite. La función debe iterar sobre la lista y sumar únicamente aquellos números que sean pares y que sean menores o iguales al límite. Si la suma supera un valor de 50 durante el proceso, la función debe detenerse inmediatamente (romper el ciclo) y devolver la suma acumulada hasta ese momento. Si el ciclo termina normalmente sin superar 50, debe devolver la suma total acumulada de los números válidos.
# difficulty: Intermedio
# expected_output: 28
# hint: Utiliza un ciclo for para recorrer la lista, estructuras condicionales (if) para verificar si es par y menor o igual al límite, y la sentencia break para salir del ciclo si la suma acumulada supera 50.

# === SOLUTION ===
def sumar_pares_con_limite(numeros, limite):
    suma_total = 0
    for num in numeros:
        if num % 2 == 0 and num <= limite:
            suma_total += num
            if suma_total > 50:
                break
    return suma_total

# === TESTS ===
try:
    assert sumar_pares_con_limite([2, 4, 6, 8, 10], 10) == 30, "Error: el test 1 ha fallado."
    assert sumar_pares_con_limite([10, 20, 30, 40], 50) == 30, "Error: considera casos límites en tu lógica."
    assert sumar_pares_con_limite([1, 3, 5, 7], 10) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")