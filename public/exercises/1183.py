# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista que contenga únicamente aquellas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. Utiliza iteración y lógica condicional.
# difficulty: Intermedio
# expected_output: ['P1rueba!', 'Python2023', 'Segura1A']
# hint: Puedes usar métodos de string como .isupper() o recorriendo los caracteres con un bucle for, además de verificar la longitud con len().

# === SOLUTION ===
def filtrar_contraseñas seguras(lista_contraseñas):
    pass

def filtrar_contraseñas(lista_contraseñas):
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
    assert filtrar_contraseñas(["abc1", "P1rueba!", "corto", "Python2023"]) == ["P1rueba!", "Python2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas(["todominusculas1", "TODOMAYUSCULAS1", "SinNumeros"]) == ["TODOMAYUSCULAS1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas(["a1B", "12345678", "ABCdefgh"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")