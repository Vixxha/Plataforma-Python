# === METADATA ===
# title: Validador y Limpiador de Hashtags
# description: Escribe una función que tome una cadena de texto, elimine los espacios sobrantes al inicio y al final, reemplace los espacios internos por guiones bajos y asegure que comience con el símbolo '#'. Si la cadena está vacía, debe retornar una cadena vacía.
# difficulty: Básico
# expected_output: "#programacion_en_python"
# hint: Puedes usar los métodos de string como strip(), split(), join() y verificar si la cadena no está vacía antes de procesarla.

# === SOLUTION ===
def limpiar_hashtag(texto):
    texto_limpio = texto.strip()
    if not texto_limpio:
        return ""
    palabras = texto_limpio.split()
    resultado = "_".join(palabras)
    return "#" + resultado

# === TESTS ===
try:
    assert limpiar_hashtag("  programacion en python  ") == "#programacion_en_python", "Error: el test 1 ha fallado."
    assert limpiar_hashtag("aprende   python ahora") == "#aprende_python_ahora", "Error: considera casos límites en tu lógica."
    assert limpiar_hashtag("") == "", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")