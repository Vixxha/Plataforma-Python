# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves "nombre", "precio" y "stock"), filtre aquellos productos que tengan un stock mayor a cero, los ordene de forma ascendente según su precio y, finalmente, busque y devuelva una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes filtrar usando list comprehensions o filter, ordenar con sorted especificando la clave 'precio', y luego extraer los nombres de los elementos que cumplan con la condición del presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    # Filtrar productos con stock mayor a 0
    en_stock = [p for p in productos if p.get("stock", 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(en_stock, key=lambda x: x["precio"])
    
    # Buscar y extraer nombres de productos dentro del presupuesto
    resultado = [p["nombre"] for p in ordenados if p["precio"] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Laptop", "precio": 1200, "stock": 5},
        {"nombre": "Mouse", "precio": 25, "stock": 10},
        {"nombre": "Teclado", "precio": 45, "stock": 0},
        {"nombre": "Monitor", "precio": 150, "stock": 3}
    ]
    assert procesar_inventario(inv1, 100) == ["Mouse"], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Libreta", "precio": 5, "stock": 20},
        {"nombre": "Lapicero", "precio": 2, "stock": 15},
        {"nombre": "Mochila", "precio": 40, "stock": 0}
    ]
    assert procesar_inventario(inv2, 10) == ["Lapicero", "Libreta"], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {"nombre": "Audífonos", "precio": 30, "stock": 2}
    ]
    assert procesar_inventario(inv3, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")