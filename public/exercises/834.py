# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un dígito numérico.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura2023']
# hint: Puedes usar un bucle para recorrer la lista y métodos de strings como .isupper() y .isdigit() combinados con bucles o condiciones para validar cada contraseña.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    seguras = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_mayuscula = False
            tiene_numero = False
            for char in pwd:
                if char.isupper():
                    tiene_mayuscula = True
                if char.isdigit():
                    tiene_numero = True
            if tiene_mayuscula and tiene_numero:
                seguras.append(pwd)
    return seguras

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Password123", "abc", "segura", "Segura2023"]) == ["Password123", "Segura2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1", "todominusculas1", "TODOMAYUSCULAS1"]) == ["TODOMAYUSCULAS1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["12345678", "abcdefgh", "A1b2c3d4"]) == ["A1b2c3d4"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")