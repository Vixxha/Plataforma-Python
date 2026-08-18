# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre y precio), filtre aquellos que tengan un precio menor o igual a un presupuesto máximo, los ordene de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista únicamente con los nombres de los productos filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtro, el método `sorted()` con una tupla o clave múltiple para el ordenamiento, y una comprensión final para extraer solo los nombres.

# === SOLUTION ===
def procesar_productos(productos, presupuesto_max):
    # Filtrar productos dentro del presupuesto
    filtrados = [p for p in productos if p['precio'] <= presupuesto_max]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    catalogo = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Monitor", "precio": 150},
        {"nombre": "Teclado", "precio": 45},
        {"nombre": "Audífonos", "precio": 45}
    ]
    
    assert procesar_productos(catalogo, 100) == ['Mouse', 'Audífonos', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_productos(catalogo, 20) == [], "Error: considera casos límites en tu lógica."
    assert procesar_productos(catalogo, 1500) == ['Mouse', 'Audífonos', 'Teclado', 'Monitor', 'Laptop'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")