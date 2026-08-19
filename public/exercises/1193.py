# === METADATA ===
# title: Validador de Contraseñas Seguras y Criterios Múltiples
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplen todos los siguientes criterios: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos un número y ningún espacio en blanco.
# difficulty: Intermedio
# expected_output: ['Pass1234', 'Python2023']
# hint: Puedes usar métodos de string como .isupper(), .isdigit(), ' ' in password y len(password). Combínalos con un bucle for y lógica condicional.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_passwords):
    passwords_validas = []
    for pwd in lista_passwords:
        if len(pwd) >= 8 and ' ' not in pwd:
            tiene_mayuscula = False
            tiene_numero = False
            for char in pwd:
                if char.isupper():
                    tiene_mayuscula = True
                if char.isdigit():
                    tiene_numero = True
            if tiene_mayuscula and tiene_numero:
                passwords_validas.append(pwd)
    return passwords_validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Pass1234", "debil", "SinNumero", "Python2023", "Con Espacio1"]) == ["Pass1234", "Python2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1A", "todominusculas1", "TODOMAYUSCULAS1"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")