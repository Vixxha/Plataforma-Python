# === METADATA ===
# title: Validador de Nombres de Usuario y Capitalización
# description: Escribe una función que reciba una cadena de texto que representa un nombre de usuario. La función debe verificar que tenga al menos 6 caracteres, no contenga espacios y devolver el nombre con la primera letra de cada palabra en mayúscula (Title Case). Si la cadena no cumple con los requisitos mínimos de longitud o contiene espacios, debe retornar la cadena "Inválido".
# difficulty: Intermedio
# expected_output: "Juan Perez"
# hint: Puedes usar los métodos de string como `.strip()`, `.split()`, `.title()` o verificar la presencia de espacios con `in`.

# === SOLUTION ===
def validar_y_capitalizar(usuario):
    if not isinstance(usuario, str):
        return "Inválido"
    
    usuario_limpio = usuario.strip()
    
    if len(usuario_limpio) < 6 or ' ' in usuario_limpio:
        return "Inválido"
        
    return usuario_limpio.title()

# === TESTS ===
try:
    assert validar_y_capitalizar("juan perez") == "Juan Perez", "Error: el test 1 ha fallado."
    assert validar_y_capitalizar("ana") == "Inválido", "Error: considera casos límites en tu lógica."
    assert validar_y_capitalizar("carlos_admin") == "Carlos_Admin", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")