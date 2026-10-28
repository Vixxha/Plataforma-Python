# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una lista de contraseñas cumple con ciertos criterios de seguridad: debe tener al menos 8 caracteres, contener al menos un número y contener al menos una letra mayúscula. La función debe retornar una lista con las contraseñas que son válidas.
# difficulty: Intermedio
# expected_output: ['Pass1234', 'Secure99']
# hint: Utiliza un bucle for para iterar sobre la lista de contraseñas y métodos de strings como .isupper(), .any() o un segundo bucle/condiciones para verificar los dígitos y la longitud.

# === SOLUTION ===
def filtrar_contraseñas(contraseñas):
    validas = []
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
                validas.append(pwd)
    return validas

# === TESTS ===
try:
    assert filtrar_contraseñas(["pass", "Pass1234", "short1A", "Secure99"]) == ["Pass1234", "Secure99"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas(["todominiscula1", "TODOMAYUSCULA1", "12345678"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas(["Abcdefg1"]) == ["Abcdefg1"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")