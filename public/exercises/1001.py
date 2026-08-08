# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista que contenga únicamente aquellas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. Utiliza iteración y lógica condicional.
# difficulty: Intermedio
# expected_output: ['P1wertyu', 'Segura2023']
# hint: Puedes usar los métodos de string como .isupper() y .isdigit() recorriendo cada carácter con un bucle for, o validando con condiciones y operadores booleanos.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    validas = []
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
                validas.append(pwd)
    return validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["P1wertyu", "corta", "sinmayusculas1", "Segura2023"]) == ["P1wertyu", "Segura2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["abc12345", "ABC12345", "A1b"]) == ["ABC12345"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["todominusc", "TODOFMAYUS", "12345678"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")