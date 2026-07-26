# === METADATA ===
# title: Analizador de Contraseñas Seguras
# description: Escribe una función que reciba una cadena de texto que representa una contraseña y verifique si cumple con tres criterios básicos de seguridad: longitud mínima de 8 caracteres, al menos una letra mayúscula y al menos un dígito numérico. La función debe retornar True si cumple todos los requisitos y False en caso contrario.
# difficulty: Intermedio
# expected_output: True para "Python2023", False para "corta1"
# hint: Puedes utilizar los métodos de string como .isupper() o .isdigit(), además de la función len().

# === SOLUTION ===
def es_contrasena_segura(password):
    if len(password) < 8:
        return False
    
    tiene_mayuscula = any(char.isupper() for char in password)
    tiene_numero = any(char.isdigit() for char in password)
    
    return tiene_mayuscula and tiene_numero

# === TESTS ===
try:
    assert es_contrasena_segura("Python2023") == True, "Error: el test 1 ha fallado."
    assert es_contrasena_segura("corta1") == False, "Error: considera casos límites en tu lógica."
    assert es_contrasena_segura("todominusculas1") == False, "Error: el caso base falló."
    assert es_contrasena_segura("SOLOMAYUSCULAS1") == True, "Error: verifica la validación de mayúsculas."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")