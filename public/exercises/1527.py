# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que evalúe si una lista de contraseñas cumple con ciertos criterios de seguridad básicos: cada contraseña debe tener al menos 8 caracteres de longitud, contener al menos un número y contener al menos una letra mayúscula. La función debe retornar una lista con las contraseñas que sean consideradas válidas.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura2023']
# hint: Puedes iterar sobre la lista de contraseñas y usar métodos de strings como isupper(), isdigit(), y una combinación de condiciones lógicas (if).

# === SOLUTION ===
def validar_contraseñas(lista_contraseñas):
    validas = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_numero = False
            tiene_mayuscula = False
            for char in pwd:
                if char.isdigit():
                    tiene_numero = True
                if char.isupper():
                    tiene_mayuscula = True
            if tiene_numero and tiene_mayuscula:
                validas.append(pwd)
    return validas

# === TESTS ===
try:
    assert validar_contraseñas(['Password123', 'corta', 'SINNUMERO', '12345678', 'Segura2023']) == ['Password123', 'Segura2023'], "Error: el test 1 ha fallado."
    assert validar_contraseñas(['abc', '123', 'defghijk']) == [], "Error: considera casos límites en tu lógica."
    assert validar_contraseñas(['MiClave1', 'OTRAClave2']) == ['MiClave1', 'OTRAClave2'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")