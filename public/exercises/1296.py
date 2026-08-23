# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan stock mayor a cero, los ordene por precio de forma ascendente, y finalmente busque y devuelva una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtrado inicial, la función sorted() con una función lambda para ordenar, y recorrer el resultado ordenado para aplicar la última condición de búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_maximo):
    # Filtrar productos con stock > 0
    en_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(en_stock, key=lambda x: x['precio'])
    
    # Filtrar por presupuesto máximo y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_maximo]
    
    return resultado

# === TESTS ===
try:
    inventario_prueba = [
        {"nombre": "Laptop", "precio": 1200, "stock": 5},
        {"nombre": "Mouse", "precio": 25, "stock": 10},
        {"nombre": "Teclado", "precio": 45, "stock": 0},
        {"nombre": "Monitor", "precio": 150, "stock": 3},
        {"nombre": "Audífonos", "precio": 30, "stock": 8}
    ]
    
    assert procesar_inventario(inventario_prueba, 50) == ["Mouse", "Audífonos"], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba, 200) == ["Mouse", "Audífonos", "Monitor"], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")