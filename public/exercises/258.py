# === METADATA ===
# title: Analizador de Números Primos y Divisores
# description: Crea una función que reciba un número entero positivo y devuelva una lista con todos sus divisores, pero filtrando solo aquellos que sean números primos.
# difficulty: Intermedio
# expected_output: Para el número 12, debería retornar [2, 3] (ya que los divisores son 1, 2, 3, 4, 6, 12).
# hint: Primero encuentra todos los divisores usando un bucle y el operador módulo (%), luego crea una lógica (o función auxiliar) para verificar si cada divisor es primo.

# === SOLUTION ===
def filtrar_divisores_primos(n):
    divisores_primos = []
    for i in range(1, n + 1):
        if n % i == 0:
            # Verificar si i es primo
            if i > 1:
                es_primo = True
                for j in range(2, int(i**0.5) + 1):
                    if i % j == 0:
                        es_primo = False
                        break
                if es_primo:
                    divisores_primos.append(i)
    return divisores_primos

# === TESTS ===
try:
    assert filtrar_divisores_primos(12) == [2, 3], "Error: el test 1 ha fallado."
    assert filtrar_divisores_primos(30) == [2, 3, 5], "Error: considera casos límites en tu lógica."
    assert filtrar_divisores_primos(7) == [7], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")