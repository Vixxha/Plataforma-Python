# === METADATA ===
# title: Validador de Contraseñas y Suma de Dígitos
# description: Escribe una función que reciba una lista de contraseñas (cadenas de texto) y retorne una nueva lista únicamente con aquellas contraseñas que cumplan con dos condiciones: tener una longitud de al menos 8 caracteres y contener al menos un dígito numérico. Además, la función debe imprimir por consola la cantidad total de contraseñas válidas encontradas utilizando un bucle.
# difficulty: Intermedio
# expected_output: ['Password123', 'secure9pass']
# hint: Puedes iterar sobre cada contraseña usando un bucle, verificar su longitud con `len()`, comprobar si tiene dígitos usando `.isdigit()` o un bucle interno, y usar condiciones `if`.

# === SOLUTION ===
def validar_contrasenias(lista_contrasenias):
    validas = []
    for pwd in lista_contrasenias:
        tiene_digito = False
        for char in pwd:
            if char.isdigit():
                tiene_digito = True
                break
        
        if len(pwd) >= 8 and tiene_digito:
            validas.append(pwd)
            
    print(f"Total válidas: {len(validas)}")
    return validas

# === TESTS ===
try:
    assert validar_contrasenias(["abc", "Password123", "short1", "secure9pass", "nodigits"]) == ["Password123", "secure9pass"], "Error: el test 1 ha fallado."
    assert validar_contrasenias(["sololetra", "12345678", "a1b2c3d4"]) == ["12345678", "a1b2c3d4"], "Error: considera casos límites en tu lógica."
    assert validar_contrasenias(["short", "abc123xyz"]) == ["abc123xyz"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")