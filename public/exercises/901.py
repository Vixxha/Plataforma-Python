# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista que contenga únicamente aquellas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos un número y al menos una letra mayúscula. La iteración y la lógica condicional son clave aquí.
# difficulty: Intermedio
# expected_output: ["Python2023", "Segura1A"]
# hint: Puedes iterar sobre la lista de contraseñas y utilizar métodos de string como .isupper(), .any() o bucles anidados junto con un bucle for principal para verificar cada condición.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    seguras = []
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
                seguras.append(pwd)
    return seguras

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Python2023", "debil", "SINnumero", "Segura1A"]) == ["Python2023", "Segura1A"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1A", "12345678", "abcdefgh"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["MiPasswordEsMuyLargaYBuena1"]) == ["MiPasswordEsMuyLargaYBuena1"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")