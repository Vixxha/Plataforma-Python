# === METADATA ===
# title: Analizador y Cifrador de Mensajes Secretos
# description: Escribe una función que tome una cadena de texto, elimine los espacios al inicio y al final, invierta las letras de cada palabra manteniendo su posición original dentro de la frase, y finalmente convierta todas las vocales a mayúsculas y las consonantes a minúsculas.
# difficulty: Intermedio
# expected_output: "hOlA mUndO" (para la entrada "  hola mundo  ")
# hint: Puedes separar la frase en palabras usando split(), luego invertir cada palabra individualmente, y finalmente usar un bucle o compresión para cambiar las mayúsculas/minúsculas de las letras.

# === SOLUTION ===
def procesar_mensaje(mensaje):
    mensaje_limpio = mensaje.strip()
    if not mensaje_limpio:
        return ""
    
    palabras = mensaje_limpio.split()
    palabras_invertidas = [palabra[::-1] for palabra in palabras]
    frase_invertida = " ".join(palabras_invertidas)
    
    vocales = "aeiouAEIOU"
    resultado = []
    
    for char in frase_invertida:
        if char.isalpha():
            if char in vocales:
                resultado.append(char.upper())
            else:
                resultado.append(char.lower())
        else:
            resultado.append(char)
            
    return "".join(resultado)

# === TESTS ===
try:
    assert procesar_mensaje("  hola mundo  ") == "AlOh OdNum", "Error: el test 1 ha fallado."
    assert procesar_mensaje("Python ES divertido") == "nOhTyp sE odItRivEd", "Error: considera casos límites en tu lógica."
    assert procesar_mensaje("AEIOU") == "UOIEA", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")