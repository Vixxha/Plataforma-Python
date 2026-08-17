# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista que contenga únicamente aquellas que cumplan con los siguientes criterios de seguridad: tener una longitud mínima de 8 caracteres, contener al menos un número y contener al menos una letra mayúscula. La iteración y la lógica condicional son clave aquí.
# difficulty: Intermedio
# expected_output: ['Abc12345', 'Python2024']
# hint: Puedes usar los métodos de string como .isupper() y .isdigit() recorriendo cada carácter de la contraseña, o verificando con bucles y condiciones anidadas.

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
    assert filtrar_contraseñas_seguras(["Abc12345", "debil", "Python2024", "sinmayusculas1"]) == ["Abc12345", "Python2024"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1A", "12345678", "ABCDEFGH"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Segura1", "OTRAsegura9", "ninguna"]) == ["Segura1", "OTRAsegura9"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")