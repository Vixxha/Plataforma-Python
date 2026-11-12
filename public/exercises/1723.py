# === METADATA ===
# title: Validador de Contraseñas y Procesador de Intentos
# description: Escribe una función que valide una lista de intentos de contraseña según tres reglas: debe tener al menos 8 caracteres, incluir al menos un dígito y contener al menos una letra mayúscula. La función debe iterar sobre la lista y retornar únicamente las contraseñas válidas.
# difficulty: Intermedio
# expected_output: ['Secure123', 'Password9']
# hint: Puedes iterar sobre cada contraseña de la lista y usar métodos de string como .isupper(), .isdigit() y len(), combinándolos con estructuras condicionales.

# === SOLUTION ===
def filtrar_contraseñas_validas(intentos):
    validas = []
    for pwd in intentos:
        if len(pwd) >= 8:
            tiene_mayus = False
            tiene_digito = False
            for char in pwd:
                if char.isupper():
                    tiene_mayus = True
                if char.isdigit():
                    tiene_digito = True
            if tiene_mayus and tiene_digito:
                validas.append(pwd)
    return validas

# === TESTS ===
try:
    assert filtrar_contraseñas_validas(["short1", "Secure123", "nounper1", "Password9"]) == ["Secure123", "Password9"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_validas(["abc", "12345678", "ABCDEFGH"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_validas(["A1b2C3d4"]) == ["A1b2C3d4"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")