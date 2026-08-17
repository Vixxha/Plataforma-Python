# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves "nombre", "precio" y "stock"), filtre aquellos que tengan stock mayor a cero, los ordene de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente busque y devuelva una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Utiliza list comprehensions o filter para el filtrado inicial, la función sorted con una clave múltiple (tupla) para el ordenamiento, y una nueva pasada para extraer los nombres que cumplan con el presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_maximo):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get("stock", 0) > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(disponibles, key=lambda x: (x["precio"], x["nombre"]))
    
    # Filtrar por presupuesto máximo y extraer solo los nombres
    resultado = [p["nombre"] for p in ordenados if p["precio"] <= presupuesto_maximo]
    
    return resultado

# === TESTS ===
try:
    inventario_prueba = [
        {"nombre": "Laptop", "precio": 1200, "stock": 5},
        {"nombre": "Mouse", "precio": 25, "stock": 10},
        {"nombre": "Teclado", "precio": 45, "stock": 0},
        {"nombre": "Monitor", "precio": 150, "stock": 2},
        {"nombre": "Audífonos", "precio": 25, "stock": 8}
    ]
    
    assert procesar_inventario(inventario_prueba, 50) == ["Audífonos", "Mouse"], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba, 200) == ["Audífonos", "Mouse", "Monitor"], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_prueba, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")