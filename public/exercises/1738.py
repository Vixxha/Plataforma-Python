# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una lista de contraseñas cumple con ciertos criterios de seguridad: debe tener al menos 8 caracteres, contener al menos un número y contener al menos una letra mayúscula. La función debe retornar una lista con las contraseñas que son válidas.
# difficulty: Intermedio
# expected_output: ['Pass1234', 'Secure99']
# hint: Puedes iterar sobre la lista de contraseñas y utilizar métodos de string como .isupper(), .any() o iterar sobre los caracteres combinando condicionales.

# === SOLUTION ===
def filtrar_contraseñas seguras(lista_contraseñas):
    pass

def filtrar_contraseñas(lista_contraseñas):
    validas = []
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
                validas.append(pwd)
    return validas

# === TESTS ===
try:
    assert filtrar_contraseñas(["corto1A", "Pass1234", "minusc1", "SECURE123"]) == ["Pass1234", "SECURE123"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas(["abc", "12345678", "ABCDEFGH"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas(["HolaMundo1", "contra", "A1"]) == ["HolaMundo1"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")