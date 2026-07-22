# === METADATA ===
# title: Validador y Limpiador de Hashtags
# description: Escribe una función que tome una frase, elimine los espacios innecesarios al inicio y al final, convierta la primera letra de cada palabra a mayúscula (formato CamelCase) y le anteponga un símbolo '#' para transformarla en un hashtag válido. Si la frase está vacía, debe retornar una cadena vacía.
# difficulty: Intermedio
# expected_output: "#ProgramacionEnPython"
# hint: Puedes usar los métodos de string como strip(), title() y replace() para limpiar y formatear el texto.

# === SOLUTION ===
def crear_hashtag(frase):
    frase_limpia = frase.strip()
    if not frase_limpia:
        return ""
    palabras = frase_limpia.split()
    hashtag = "#" + "".join([p.capitalize() for p in palabras])
    return hashtag

# === TESTS ===
try:
    assert crear_hashtag("  programacion en python  ") == "#ProgramacionEnPython", "Error: el test 1 ha fallado."
    assert crear_hashtag("¡hola mundo!") == "#¡HolaMundo!", "Error: considera casos límites en tu lógica."
    assert crear_hashtag("   ") == "", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")