# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista que contenga únicamente aquellas que cumplen con los siguientes criterios de seguridad: tener al menos 8 caracteres de longitud, contener al menos un dígito numérico y contener al menos una letra mayúscula. Utiliza bucles y lógica condicional.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura2024']
# hint: Puedes recorrer la lista con un bucle for y usar métodos de cadenas como .isupper() y .isdigit() junto con condicionales para validar cada regla.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    contraseñas_validas = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_mayuscula = False
            tiene_digito = False
            for char in pwd:
                if char.isupper():
                    tiene_mayuscula = True
                if char.isdigit():
                    tiene_digito = True
            if tiene_mayuscula and tiene_digito:
                contraseñas_validas.append(pwd)
    return contraseñas_validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["corto1A", "Password123", "minusk", "Segura2024"]) == ["Password123", "Segura2024"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["sinmayusculas1", "SOLOMAYUSCULAS1", "12345678"]) == ["SOLOMAYUSCULAS1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["abc", "123", "ABC"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")