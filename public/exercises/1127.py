# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplen con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un número. Utiliza iteración y lógica condicional.
# difficulty: Intermedio
# expected_output: ['P1assword', 'Segura2023']
# hint: Puedes usar bucles `for` para recorrer la lista y métodos de string como `.isupper()`, `.islower()`, y `.isdigit()`.

# === SOLUTION ===
def filtrar_contraseñas_seguras(contraseñas):
    seguras = []
    for pwd in contraseñas:
        if len(pwd) >= 8:
            tiene_mayus = False
            tiene_minus = False
            tiene_num = False
            for char in pwd:
                if char.isupper():
                    tiene_mayus = True
                elif char.islower():
                    tiene_minus = True
                elif char.isdigit():
                    tiene_num = True
            if tiene_mayus and tiene_minus and tiene_num:
                seguras.append(pwd)
    return seguras

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["corto1A", "P1assword", "todominusculas1", "SINNUMEROS"]) == ["P1assword"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["Segura2023", "abc", "12345678", "ABCDEFGH"]) == ["Segura2023"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")