# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista que contenga únicamente aquellas que cumplen con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un número. Utiliza bucles y lógica condicional para evaluarlas.
# difficulty: Intermedio
# expected_output: ['Password123', 'SecurePass9']
# hint: Puedes usar los métodos de string como .isupper(), .isdigit(), y recorrer la lista con un bucle for combinando condiciones if.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    contraseñas_validas = []
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
                contraseñas_validas.append(pwd)
    return contraseñas_validas

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["Password123", "weak", "NoNumberHere", "SecurePass9"]) == ["Password123", "SecurePass9"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["short1", "ALLUPPER1", "alllower1", "12345678"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Valid1pass", "abc"]) == ["Valid1pass"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")