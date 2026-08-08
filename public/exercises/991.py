# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplan los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. Utiliza bucles y lógica condicional.
# difficulty: Intermedio
# expected_output: ['Password123', 'PyThOn2023']
# hint: Puedes recorrer la lista con un bucle for y usar métodos de strings como .isupper() y .isdigit() combinados con bucles o condicionales para validar cada carácter.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_passwords):
    passwords_seguras = []
    for pwd in lista_passwords:
        if len(pwd) >= 8:
            tiene_mayuscula = False
            tiene_numero = False
            for char in pwd:
                if char.isupper():
                    tiene_mayuscula = True
                if char.isdigit():
                    tiene_numero = True
            if tiene_mayuscula and tiene_numero:
                passwords_seguras.append(pwd)
    return passwords_seguras

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Password123", "abc", "ABC", "PyThOn2023"]) == ["Password123", "PyThOn2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1", "sinmayusculas1", "SOLOMAYUSCULAS"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["A1bcdefg", "12345678A"]) == ["A1bcdefg", "12345678A"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")