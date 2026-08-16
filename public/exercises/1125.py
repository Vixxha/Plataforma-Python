# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplan los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número.
# difficulty: Intermedio
# expected_output: ['Perrito123', 'Gato$456']
# hint: Puedes recorrer la lista con un bucle for y usar los métodos de string como .isupper() y .isdigit() combinados con bucles o condicionales.

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
    assert filtrar_contraseñas_seguras(["corto", "SinNumero", "Perrito123", "Gato$456", "12345678"]) == ["Perrito123", "Gato$456"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["abc", "DEF", "123"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Python2023", "python2023", "PYTHON"]) == ["Python2023"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")