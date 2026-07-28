# === METADATA ===
# title: Analizador y Validador de Nombres de Usuario
# description: Escribe una función que reciba un string con un nombre de usuario y valide si cumple con lo siguiente: debe tener entre 6 y 12 caracteres (inclusive), solo debe contener letras minúsculas y números (sin espacios ni símbolos especiales), y debe retornar el nombre en formato de título (primera letra en mayúscula y el resto en minúsculas) solo si es válido; de lo contrario, debe retornar un mensaje de error que sea "Inválido".
# difficulty: Intermedio
# expected_output: "Python2023" (para la entrada "python2023") o "Inválido" (para la entrada "py!")
# hint: Utiliza los métodos de string como isalnum(), islower(), y las propiedades de slicing o len() para verificar la longitud antes de aplicar capitalize().

# === SOLUTION ===
def validar_y_formatear_usuario(username):
    if not (6 <= len(username) <= 12):
        return "Inválido"
    if not username.isalnum() or not username.islower():
        return "Inválido"
    return username.capitalize()

# === TESTS ===
try:
    assert validar_y_formatear_usuario("python2023") == "Python2023", "Error: el test 1 ha fallado."
    assert validar_y_formatear_usuario("py!") == "Inválido", "Error: considera casos límites en tu lógica."
    assert validar_y_formatear_usuario("ADMIN123") == "Inválido", "Error: el caso base falló."
    assert validar_y_formatear_usuario("corta") == "Inválido", "Error: la validación de longitud falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")