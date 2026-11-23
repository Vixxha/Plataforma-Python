# === METADATA ===
# title: Validador de Contraseñas y Intentos
# description: Escribe una función que valide una contraseña ingresada como lista de caracteres o string, aplicando reglas de lógica condicional (longitud mínima de 6, al menos una mayúscula y un número). Además, simula un proceso iterativo que procese una lista de intentos de contraseña y devuelva una lista con los resultados booleanos de la validación para cada uno.
# difficulty: Intermedio
# expected_output: [True, False, True]
# hint: Puedes iterar sobre la lista de contraseñas y, para cada una, usar bucles o condiciones para verificar los requisitos de mayúsculas, dígitos y longitud.

# === SOLUTION ===
def validar_contraseñas(intentos):
    resultados = []
    for pwd in intentos:
        if not isinstance(pwd, str) or len(pwd) < 6:
            resultados.append(False)
            continue
        
        tiene_mayuscula = False
        tiene_numero = False
        
        for char in pwd:
            if char.isupper():
                tiene_mayuscula = True
            elif char.isdigit():
                tiene_numero = True
                
        if tiene_mayuscula and tiene_numero:
            resultados.append(True)
        else:
            resultados.append(False)
            
    return resultados

# === TESTS ===
try:
    assert validar_contraseñas(["Pass1", "abc", "PASSWORD99", "123456"]) == [True, False, True, False], "Error: el test 1 ha fallado."
    assert validar_contraseñas(["short1", "A1", "Valid123"]) == [False, False, True], "Error: considera casos límites en tu lógica."
    assert validar_contraseñas([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")