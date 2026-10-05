# === METADATA ===
# title: Validador de Secuencias Collatz Inversas
# description: Escribe una función que reciba un número entero positivo y calcule cuántos pasos requiere la famosa Conjetura de Collatz para llegar a 1. Si el número es par, se divide entre 2; si es impar, se multiplica por 3 y se suma 1. Si se recibe un número menor o igual a 0, la función debe retornar -1.
# difficulty: Intermedio
# expected_output: 7
# hint: Utiliza un bucle while para repetir las operaciones condicionales y un contador para llevar el registro de los pasos. No olvides validar el caso de entrada inválida.

# === SOLUTION ===
def contar_pasos_collatz(n):
    if n <= 0:
        return -1
    
    pasos = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1
        
    return pasos

# === TESTS ===
try:
    assert contar_pasos_collatz(6) == 8, "Error: el test 1 ha fallado."
    assert contar_pasos_collatz(1) == 0, "Error: considera casos límites en tu lógica."
    assert contar_pasos_collatz(-5) == -1, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")