# === METADATA ===
# title: Mayor de edad
# description: Escribe una función 'verificar_edad' que reciba una edad (entero) y retorne si la persona es mayor o menor de edad.
# expected_output: 18 o más debe devolver "Eres mayor de edad.", menos de 18 debe devolver "Aún eres menor de edad."
# hint: Usa una estructura condicional if/else para comparar la edad.

# === SOLUTION ===
def verificar_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad."
    else:
        return "Aún eres menor de edad."

# === TESTS ===
try:
    assert verificar_edad(18) == "Eres mayor de edad.", "Error con edad 18"
    assert verificar_edad(25) == "Eres mayor de edad.", "Error con edad 25"
    assert verificar_edad(17) == "Aún eres menor de edad.", "Error con edad 17"
    assert verificar_edad(0) == "Aún eres menor de edad.", "Error con edad 0"
except NameError:
    raise AssertionError("La función 'verificar_edad' no está definida.")