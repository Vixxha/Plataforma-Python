# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre, precio, stock), filtre aquellos que tengan stock mayor a cero, los ordene de forma ascendente según su precio y finalmente devuelva una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes usar list comprehensions o filter para el filtrado inicial, la función sorted con una función lambda para ordenar, y un ciclo o búsqueda para extraer los nombres según el presupuesto.

# === SOLUTION ===
def procesar_productos(productos, presupuesto_maximo):
    # Filtrar productos con stock mayor a 0
    con_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(con_stock, key=lambda x: x['precio'])
    
    # Filtrar y extraer nombres cuyo precio sea menor o igual al presupuesto máximo
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_maximo]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {"nombre": "Monitor", "precio": 200, "stock": 5},
        {"nombre": "Mouse", "precio": 25, "stock": 10},
        {"nombre": "Teclado", "precio": 45, "stock": 0},
        {"nombre": "Audífonos", "precio": 30, "stock": 2}
    ]
    
    assert procesar_productos(inventario, 50) == ["Mouse", "Audífonos"], "Error: el test 1 ha fallado."
    assert procesar_productos(inventario, 20) == [], "Error: considera casos límites en tu lógica."
    assert procesar_productos([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")