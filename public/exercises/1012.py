# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas (cadenas de texto) y devuelva una nueva lista con aquellas que cumplan todas las siguientes condiciones para ser consideradas seguras: tener al menos 8 caracteres de longitud, contener al menos un número y contener al menos una letra mayúscula. La iteración y la lógica condicional son clave aquí.
# difficulty: Intermedio
# expected_output: ['Password123', 'Python2024']
# hint: Puedes iterar sobre cada contraseña de la lista, evaluar su longitud, y usar los métodos .isdigit() y .isupper() recorriendo los caracteres o combinándolos con la función any().

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    seguras = []
    for pwd in lista_contraseñas:
        if len(pwd) >= 8:
            tiene_numero = False
            tiene_mayuscula = False
            for char in pwd:
                if char.isdigit():
                    tiene_numero = True
                if char.isupper():
                    tiene_mayuscula = True
            if tiene_numero and tiene_mayuscula:
                seguras.append(pwd)
    return seguras

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Password123", "abc", "PYTHON", "contraseña", "Python2024"]) == ["Password123", "Python2024"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corta1A", "solonumeros123", "SOLOMAYUSCULAS"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Abcdefg1", "12345678A", "A1b2C3d4"]) == ["Abcdefg1", "12345678A", "A1b2C3d4"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")