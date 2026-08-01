# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplen con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. Utiliza bucles y lógica condicional.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura2024']
# hint: Puedes usar métodos de string como .isupper() y .isdigit() recorriendo cada carácter con un bucle for, o combinándolos con funciones como any().

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
    assert filtrar_contraseñas_seguras(["Password123", "deb", "sinnumero", "Segura2024"]) == ["Password123", "Segura2024"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1A", "todominusculas1", "TODOMAYUSCULAS1"]) == ["TODOMAYUSCULAS1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["abc", "123", "ABC"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")