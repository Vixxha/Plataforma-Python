# === METADATA ===
# title: Validador y Normalizador de Nombres de Usuario
# description: Escribe una función que tome una cadena que representa un nombre de usuario, elimine los espacios en blanco al inicio y al final, reemplace cualquier espacio interno por un guion bajo '_', y devuelva el resultado completamente en minúsculas. Si la cadena está vacía o solo contiene espacios, debe devolver "inválido".
# difficulty: Intermedio
# expected_output: "juan_perez"
# hint: Puedes usar los métodos de string en Python como .strip(), .replace(), .lower() y verificar si la cadena resultante queda vacía.

# === SOLUTION ===
def normalizar_usuario(texto):
    if not texto or not texto.strip():
        return "inválido"
    
    # Limpiar espacios en los extremos, reemplazar espacios internos y convertir a minúsculas
    texto_limpio = texto.strip()
    texto_procesado = texto_limpio.replace(" ", "_").lower()
    
    return texto_procesado

# === TESTS ===
try:
    assert normalizar_usuario("  Juan Perez  ") == "juan_perez", "Error: el test 1 ha fallado."
    assert normalizar_usuario("MARIA GOMEZ") == "maria_gomez", "Error: considera casos límites en tu lógica."
    assert normalizar_usuario("   ") == "inválido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")