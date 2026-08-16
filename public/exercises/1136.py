# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplen con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. Utiliza bucles y lógica condicional.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura2024']
# hint: Puedes usar métodos de strings como .isupper() y .isdigit() recorriendo cada carácter con un bucle for, o combinándolos con funciones como any().

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    seguras = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_mayus = False
            tiene_num = False
            for char in pwd:
                if char.isupper():
                    tiene_mayus = True
                if char.isdigit():
                    tiene_num = True
            if tiene_mayus and tiene_num:
                seguras.append(pwd)
    return seguras

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Password123", "debil", "SINnumero", "Segura2024"]) == ["Password123", "Segura2024"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["abc", "12345678", "ABCDEFGH"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Python2023", "A1b2C3d4"]) == ["Python2023", "A1b2C3d4"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")