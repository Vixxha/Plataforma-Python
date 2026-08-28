# === METADATA ===
# title: Analizador y Validador de Correos Electrónicos
# description: Escribe una función que reciba una cadena de texto que representa un correo electrónico. La función debe validar y formatear el string: debe verificar que contenga exactamente un símbolo '@', que el nombre de usuario y el dominio no estén vacíos, y devolver el correo en minúsculas y sin espacios en blanco al inicio o al final. Si el correo no es válido, debe retornar "Correo inválido".
# difficulty: Intermedio
# expected_output: "usuario@dominio.com"
# hint: Utiliza métodos de strings como strip(), lower(), count() y split() para verificar las condiciones paso a paso.

# === SOLUTION ===
def validar_y_formatear_correo(email):
    if not isinstance(email, str):
        return "Correo inválido"
    
    email_limpio = email.strip().lower()
    
    if email_limpio.count('@') != 1:
        return "Correo inválido"
    
    partes = email_limpio.split('@')
    usuario = partes[0]
    dominio = partes[1]
    
    if not usuario or not dominio:
        return "Correo inválido"
    
    if '.' not in dominio:
        return "Correo inválido"
        
    return email_limpio

# === TESTS ===
try:
    assert validar_y_formatear_correo("  USUARIO@Dominio.COM  ") == "usuario@dominio.com", "Error: el test 1 ha fallado."
    assert validar_y_formatear_correo("correo.invalido.com") == "Correo inválido", "Error: considera casos límites en tu lógica."
    assert validar_y_formatear_correo("test@@dominio.com") == "Correo inválido", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")