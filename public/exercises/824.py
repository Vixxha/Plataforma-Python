# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de cadenas (contraseñas) y devuelva una nueva lista únicamente con aquellas contraseñas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. Utiliza iteración y lógica condicional.
# difficulty: Intermedio
# expected_output: ['Contrasena1', 'Segura2023']
# hint: Puedes recorrer la lista con un bucle o comprensión de lista, y utilizar métodos de cadena como .isupper(), .isdigit() y un bucle interno o la función any() para evaluar cada carácter.

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
    assert filtrar_contraseñas_seguras(["abc", "Contrasena1", "segura", "Segura2023", "12345678"]) == ["Contrasena1", "Segura2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["corto1", "MAYUSCULAS1", "minusculas1"]) == ["MAYUSCULAS1", "minusculas1"], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["sololetras", "123456789", "no"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")