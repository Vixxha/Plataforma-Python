# === METADATA ===
# title: Validador de Contraseña Segura
# description: Escribe una función que reciba una lista de cadenas (contraseñas) y devuelva una nueva lista que contenga únicamente aquellas contraseñas que cumplan con las siguientes reglas: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. Utiliza iteración y lógica condicional.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura2023']
# hint: Puedes usar los métodos de string como .isupper() y .isdigit() junto con un bucle for y condicionales if.

# === SOLUTION ===
def filtrar_contraseñas_seguras(passwords):
    validas = []
    for pwd in passwords:
        if len(pwd) >= 8:
            tiene_mayus = False
            tiene_num = False
            for char in pwd:
                if char.isupper():
                    tiene_mayus = True
                if char.isdigit():
                    tiene_num = True
            if tiene_mayus and tiene_num:
                validas.append(pwd)
    return validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["corto1", "Password123", "todominusculas1", "SOLONUMEROS123"]) == ["Password123", "SOLONUMEROS123"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["abc", "12345678", "ABCDEFGH"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Segura2023", "debil", "OtraMas9"]) == ["Segura2023", "OtraMas9"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")