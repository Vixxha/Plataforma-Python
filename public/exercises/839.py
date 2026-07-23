# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas (strings) y devuelva una nueva lista que contenga únicamente aquellas contraseñas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. Utiliza iteración y lógica condicional.
# difficulty: Intermedio
# expected_output: ['Password123', 'Segura2023*']
# hint: Puedes recorrer la lista con un bucle o comprensión, y para cada string utilizar métodos de string como .isupper(), .isdigit(), y la función len().

# === SOLUTION ===
def filtrar_contraseñas_seguras(passwords):
    seguras = []
    for pwd in passwords:
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
    assert filtrar_contraseñas_seguras(["abc", "Password123", "short1", "Segura2023*"]) == ["Password123", "Segura2023*"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["todominisculas1", "TODOMAYUSCULAS1", "sinnumeros"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")