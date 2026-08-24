# === METADATA ===
# title: Validador de Contraseñas y Suma de Dígitos
# description: Escribe una función que reciba una lista de contraseñas (cadenas de texto) y devuelva una nueva lista con aquellas contraseñas que cumplan todas las siguientes condiciones: tener al menos 8 caracteres, contener al menos un número y contener al menos una letra mayúscula. Además, por cada contraseña válida, debes sumar todos los dígitos numéricos que contenga en un total acumulado, y la función debe retornar una tupla con la lista de contraseñas válidas y la suma total de sus dígitos.
# difficulty: Intermedio
# expected_output: (['Python2023', 'Segura9Pass'], 26)
# hint: Utiliza bucles for para recorrer la lista y los caracteres, y métodos de cadena como .isupper() y .isdigit() para evaluar las condiciones.

# === SOLUTION ===
def procesar_contrasenias(contrasenias):
    validas = []
    suma_digitos = 0
    
    for pwd in contrasenias:
        if len(pwd) >= 8:
            tiene_mayus = False
            tiene_num = False
            digitos_pwd = 0
            
            for char in pwd:
                if char.isupper():
                    tiene_mayus = True
                if char.isdigit():
                    tiene_num = True
                    digitos_pwd += int(char)
            
            if tiene_mayus and tiene_num:
                validas.append(pwd)
                suma_digitos += digitos_pwd
                
    return (validas, suma_digitos)

# === TESTS ===
try:
    assert procesar_contrasenias(["Python2023", "corta", "todominusculas1", "Segura9Pass"]) == (['Python2023', 'Segura9Pass'], 26), "Error: el test 1 ha fallado."
    assert procesar_contrasenias(["abc", "12345678", "ABCDEFGH"]) == ([], 0), "Error: considera casos límites en tu lógica."
    assert procesar_contrasenias(["Clave1", "MiPasswordEsMuyLargaYSegura1"]) == (['MiPasswordEsMuyLargaYSegura1', 'Clave1'], 2), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")