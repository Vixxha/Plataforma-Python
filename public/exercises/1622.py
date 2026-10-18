# === METADATA ===
# title: Verificador de Números Primos y Divisores
# description: Escribe una función que determine si un número entero positivo es primo. Un número primo es aquel que solo es divisible por sí mismo y por 1. Si no es primo, la función debe devolver la cantidad de divisores propios que tiene (excluyendo al 1 y al propio número). Si es primo, debe devolver la cadena "Es primo".
# difficulty: Intermedio
# expected_output: "Es primo" para el número 7, y 2 para el número 4 (sus divisores propios son 2).
# hint: Puedes iterar desde 2 hasta la raíz cuadrada del número para verificar si existen divisores.

# === SOLUTION ===
def verificar_primo_o_divisores(n):
    if n <= 1:
        return 0
    
    divisores = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisores.append(i)
            if i != n // i:
                divisores.append(n // i)
                
    if len(divisores) == 0:
        return "Es primo"
    else:
        return len(divisores)

# === TESTS ===
try:
    assert verificar_primo_o_divisores(7) == "Es primo", "Error: el test 1 ha fallado."
    assert verificar_primo_o_divisores(4) == 1, "Error: considera casos límites en tu lógica."
    assert verificar_primo_o_divisores(12) == 4, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")