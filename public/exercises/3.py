# === METADATA ===
# title: Invertir cadena
# description: Escribe una función 'invertir' que reciba un texto (string) y retorne el mismo texto escrito al revés. No uses trucos de Python como texto[::-1] y hazlo con un ciclo loop.
# expected_output: "hola" debe devolver "aloh"
# hint: Crea un string vacío y, en un ciclo for, ve sumando cada letra nueva ANTES del texto que ya tienes guardado.
# === SOLUTION ===
def invertir(texto):
    resultado = ""
    for letra in texto:
        resultado = letra + resultado
    return resultado

# === TESTS ===
try:
    assert invertir("hola") == "aloh", "Error: 'hola' invertido debe ser 'aloh'"
    assert invertir("hacker") == "rekcah", "Error: 'hacker' invertido debe ser 'rekcah'"
    assert invertir("") == "", "Error: texto vacío debe devolver vacío"
except NameError:
    raise AssertionError("La función 'invertir' no está definida.")
