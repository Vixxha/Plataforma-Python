# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre y precio), filtre aquellos que tengan un precio menor o igual a un presupuesto máximo, los ordene de forma ascendente según su precio y finalmente devuelva una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtro, la función sorted() con una función lambda para ordenar por precio, y otra list comprehension para extraer solo los nombres.

# === SOLUTION ===
def procesar_productos(productos, presupuesto_max):
    # Filtrar productos cuyo precio sea menor o igual al presupuesto
    filtrados = [p for p in productos if p['precio'] <= presupuesto_max]
    
    # Ordenar los productos filtrados por precio de forma ascendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    
    # Extraer únicamente los nombres de los productos ordenados
    nombres = [p['nombre'] for p in ordenados]
    
    return nombres

# === TESTS ===
try:
    inventario = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Monitor", "precio": 150},
        {"nombre": "Teclado", "precio": 45},
        {"nombre": "Impresora", "precio": 200}
    ]
    
    assert procesar_productos(inventario, 100) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_productos(inventario, 500) == ['Mouse', 'Teclado', 'Monitor', 'Impresora'], "Error: considera casos límites en tu lógica."
    assert procesar_productos(inventario, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")