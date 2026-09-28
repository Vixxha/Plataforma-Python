# === METADATA ===
# title: Analizador y Validador de Nombres de Usuario
# description: Escribe una función que tome una cadena que representa un nombre de usuario y verifique si cumple con los siguientes criterios: debe tener una longitud entre 5 y 15 caracteres (inclusive), solo debe contener caracteres alfanuméricos (letras y números), y debe retornar el nombre de usuario completamente en minúsculas si es válido, o la cadena "INVÁLIDO" si no cumple con las reglas.
# difficulty: Intermedio
# expected_output: "usuario123" o "INVÁLIDO"
# hint: Puedes usar los métodos de string como .isalnum() y .lower(), además de la función len().

# === SOLUTION ===
def validar_usuario(nombre):
    if 5 <= len(nombre) <= 15 and nombre.isalnum():
        return nombre.lower()
    return "INVÁLIDO"

# === TESTS ===
try:
    assert validar_usuario("Python123") == "python123", "Error: el test 1 ha fallado."
    assert validar_usuario("User_name") == "INVÁLIDO", "Error: considera casos límites en tu lógica."
    assert validar_usuario("abc") == "INVÁLIDO", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")