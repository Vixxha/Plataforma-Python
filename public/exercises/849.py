# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre, precio, stock), filtre aquellos que tengan stock mayor a cero, los ordene por precio de forma ascendente y finalmente busque y devuelva una lista solo con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para el ordenamiento, y recorrer la lista resultante para extraer los nombres que cumplan con el presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    # Filtrar productos con stock > 0
    en_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(en_stock, key=lambda x: x['precio'])
    
    # Buscar y extraer nombres de productos dentro del presupuesto
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inventario_1 = [
        {"nombre": "Monitor", "precio": 150.0, "stock": 5},
        {"nombre": "Teclado", "precio": 30.0, "stock": 10},
        {"nombre": "Mouse", "precio": 20.0, "stock": 0},
        {"nombre": "Laptop", "precio": 800.0, "stock": 2},
        {"nombre": "Audífonos", "precio": 45.0, "stock": 8}
    ]
    
    assert procesar_inventario(inventario_1, 50) == ["Teclado", "Audífonos"], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_1, 200) == ["Teclado", "Audífonos", "Monitor"], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_1, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")