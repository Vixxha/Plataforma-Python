# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas (strings) y devuelva una nueva lista que contenga únicamente aquellas contraseñas que cumplan con las siguientes reglas: tener al menos 8 caracteres de longitud, contener al menos un número y contener al menos una letra mayúscula. La iteración y la lógica condicional son clave aquí.
# difficulty: Intermedio
# expected_output: ['Password1', 'Segura2023']
# hint: Puedes usar los métodos de string como .isupper(), .isdigit() y la función len() combinados con un bucle for o una comprensión de listas.

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
    assert filtrar_contraseñas_seguras(["Password1", "debil", "12345678", "Segura2023", "abcD"]) == ["Password1", "Segura2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["todominusculas1", "TODOMAYUSCULAS1", "SinNumeros"]) == ["TODOMAYUSCULAS1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["cort1", "aB1", "longitudvalida1"]) == ["longitudvalida1"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")