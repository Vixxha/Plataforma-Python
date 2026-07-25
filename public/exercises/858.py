# === METADATA ===
# title: Validador de Nombres de Usuario y Capitalización
# description: Escribe una función que reciba una cadena con el nombre de usuario, elimine los espacios en blanco al inicio y al final, verifique que su longitud esté entre 5 y 15 caracteres (inclusive), y devuelva el nombre con la primera letra de cada palabra en mayúscula (formato título). Si no cumple con la longitud requerida, la función debe devolver "Inválido".
# difficulty: Básico
# expected_output: "Ana Maria"
# hint: Recuerda usar métodos de strings como strip(), title() y len() para validar la longitud.

# === SOLUTION ===
def procesar_usuario(nombre):
    nombre_limpio = nombre.strip()
    if 5 <= len(nombre_limpio) <= 15:
        return nombre_limpio.title()
    return "Inválido"

# === TESTS ===
try:
    assert procesar_usuario("  ana maria  ") == "Ana Maria", "Error: el test 1 ha fallado."
    assert procesar_usuario("carlos") == "Carlos", "Error: considera casos límites en tu lógica."
    assert procesar_usuario("  ia  ") == "Inválido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")