# === METADATA ===
# title: Analizador de Mensajes Cifrados
# description: Escribe una función que reciba un string de texto, elimine los espacios sobrantes al inicio y al final, invierta el orden de las palabras (no de las letras individuales) y finalmente convierta todo el texto a minúsculas.
# difficulty: Intermedio
# expected_output: "mundo hola"
# hint: Puedes usar los métodos de string como `.strip()`, `.split()` y el operador de unión junto con inversión de listas `[::-1]`.

# === SOLUTION ===
def procesar_mensaje(texto):
    texto_limpio = texto.strip()
    palabras = texto_limpio.split()
    palabras_invertidas = palabras[::-1]
    return " ".join(palabras_invertidas).lower()

# === TESTS ===
try:
    assert procesar_mensaje("  Hola Mundo  ") == "mundo hola", "Error: el test 1 ha fallado."
    assert procesar_mensaje("PYTHON es GENIAL") == "genial es python", "Error: considera casos límites en tu lógica."
    assert procesar_mensaje("  Programar   es   divertido  ") == "divertido es programar", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")