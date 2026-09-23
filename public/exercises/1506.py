# === METADATA ===
# title: Validador de Contraseñas Seguras y Contador de Intentos
# description: Escribe una función que reciba una lista de contraseñas y valide cada una según reglas básicas. Una contraseña es válida si tiene al menos 8 caracteres, contiene al menos un dígito y al menos una letra mayúscula. La función debe iterar sobre la lista y retornar cuántas contraseñas cumplen con todos los requisitos.
# difficulty: Intermedio
# expected_output: 2
# hint: Usa un bucle 'for' para recorrer la lista, condicionales 'if' para verificar cada regla, y métodos de string como .isupper() o .isdigit().

# === SOLUTION ===
def contar_contraseñas_seguras(contraseñas):
    validas = 0
    for pwd in contraseñas:
        if len(pwd) >= 8:
            tiene_mayus = False
            tiene_digito = False
            for char in pwd:
                if char.isupper():
                    tiene_mayus = True
                if char.isdigit():
                    tiene_digito = True
            if tiene_mayus and tiene_digito:
                validas += 1
    return validas

# === TESTS ===
try:
    assert contar_contraseñas_seguras(["Password123", "corto1A", "SOLOPROGRAMO"]) == 1, "Error: el test 1 ha fallado."
    assert contar_contraseñas_seguras(["Abc12345", "MiClaveSegura1", "12345678"]) == 2, "Error: considera casos límites en tu lógica."
    assert contar_contraseñas_seguras(["deb", "abcxyz12", "MAYUSCULAS"]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")