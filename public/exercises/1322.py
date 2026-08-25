# === METADATA ===
# title: Validador de Contraseñas Seguras y Cómputo de Intentos
# description: Escribe una función que reciba una lista de contraseñas y devuelva cuántas de ellas cumplen con los criterios de seguridad: longitud mínima de 8 caracteres, al menos un dígito numérico y al menos una letra mayúscula. Utiliza bucles y lógica condicional.
# difficulty: Intermedio
# expected_output: 2
# hint: Usa un bucle para iterar sobre la lista y condiciones (if) con métodos de string como .isupper() y .isdigit() para validar cada regla.

# === SOLUTION ===
def contar_contraseñas_seguras(contraseñas):
    seguras = 0
    for pwd in contraseñas:
        if len(pwd) >= 8:
            tiene_mayuscula = False
            tiene_numero = False
            for char in pwd:
                if char.isupper():
                    tiene_mayuscula = True
                if char.isdigit():
                    tiene_numero = True
            if tiene_mayuscula and tiene_numero:
                seguras += 1
    return seguras

# === TESTS ===
try:
    assert contar_contraseñas_seguras(["Password123", "corto1", "SOLONUMEROS123", "abc12345"]) == 2, "Error: el test 1 ha fallado."
    assert contar_contraseñas_seguras(["contra", "sinmayusculas1", "TODOMAYUSCULAS1"]) == 1, "Error: considera casos límites en tu lógica."
    assert contar_contraseñas_seguras(["Ab1", "Short1A"]) == 1, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")