# === METADATA ===
# title: Validador de Contraseñas Seguras
# description: Escribe una función que reciba una lista de contraseñas y devuelva una nueva lista solo con aquellas que cumplan con los siguientes criterios de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un dígito numérico.
# difficulty: Intermedio
# expected_output: ["Clave1234", "Python2023"]
# hint: Puedes usar métodos de strings como .isupper(), .islower(), .isdigit() y un bucle for combinados con condicionales.

# === SOLUTION ===
def filtrar_contraseñas_seguras(lista_contraseñas):
    contraseñas_seguras = []
    for password in lista_contraseñas:
        if len(password) >= 8:
            tiene_mayuscula = False
            tiene_minuscula = False
            tiene_digito = False
            for char in password:
                if char.isupper():
                    tiene_mayuscula = True
                elif char.islower():
                    tiene_minuscula = True
                elif char.isdigit():
                    tiene_digito = True
            
            if tiene_mayuscula and tiene_minuscula and tiene_digito:
                contraseñas_seguras.append(password)
                
    return contraseñas_seguras

# === TESTS ===
try:
    assert filtrar_contraseñas_seguras(["corto", "Clave1234", "minusc1234", "MAYUSC1234", "Python2023"]) == ["Clave1234", "Python2023"], "Error: el test 1 ha fallado."
    assert filtrar_contraseñas_seguras(["abc", "12345678", "ABCDEFGH"]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_contraseñas_seguras(["Segura1", "aB2", "SuperSecreto99"]) == ["Segura1", "SuperSecreto99"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")