# === METADATA ===
# title: Analizador de Calificaciones
# description: Escribe una función que reciba una lista de calificaciones numéricas (enteros o flotantes entre 0 y 100). Utiliza bucles y lógica condicional para calcular el promedio y retornar una letra de calificación basada en el promedio: 'A' si es mayor o igual a 90, 'B' si es mayor o igual a 80 y menor a 90, 'C' si es mayor o igual a 70 y menor a 80, 'D' si es mayor o igual a 60 y menor a 70, y 'F' si es menor a 60. Si la lista está vacía, debe retornar 'F'.
# difficulty: Intermedio
# expected_output: 'B'
# hint: Usa un bucle para sumar los elementos y la función len() para el promedio. Asegúrate de manejar el caso de una lista vacía para evitar divisiones entre cero.

# === SOLUTION ===
def analizar_calificaciones(calificaciones):
    if not calificaciones:
        return 'F'
    
    suma = 0
    cantidad = 0
    for nota in calificaciones:
        suma += nota
        cantidad += 1
        
    promedio = suma / cantidad
    
    if promedio >= 90:
        return 'A'
    elif promedio >= 80:
        return 'B'
    elif promedio >= 70:
        return 'C'
    elif promedio >= 60:
        return 'D'
    else:
        return 'F'

# === TESTS ===
try:
    assert analizar_calificaciones([85, 90, 95]) == 'A', "Error: el test 1 ha fallado."
    assert analizar_calificaciones([70, 75, 80]) == 'C', "Error: considera casos límites en tu lógica."
    assert analizar_calificaciones([]) == 'F', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")