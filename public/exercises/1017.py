# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un dígito numérico.
# difficulty: Intermedio
# expected_output: ['P1nc3lazo!', 'Python2023']
# hint: Utiliza bucles para recorrer la lista, condicionales para verificar cada regla, y métodos de cadenas como .isupper(), .islower() e .isdigit().

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_passwords):
    passwords_validas = []
    for pwd in lista_passwords:
        if len(pwd) >= 8:
            tiene_mayus = False
            tiene_minus = False
            tiene_digito = False
            for char in pwd:
                if char.isupper():
                    tiene_mayus = True
                elif char.islower():
                    tiene_minus = True
                elif char.isdigit():
                    tiene_digito = True
            if tiene_mayus and tiene_minus and tiene_digito:
                passwords_validas.append(pwd)
    return passwords_validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["corto1A", "P1nc3lazo!", "solo_minusculas", "SOLOMAYUSCULAS1", "Python2023"]) == ["P1nc3lazo!", "Python2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["abc", "12345", "ABCDE"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Passw0rd"]) == ["Passw0rd"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")