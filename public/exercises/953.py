# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre, precio y stock), filtre aquellos que tengan stock mayor a cero, los ordene de menor a mayor precio (y en caso de empate, alfabéticamente por nombre) y finalmente busque y devuelva únicamente una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes usar las funciones integradas de Python como 'filter' o comprensiones de lista, el método 'sort()' con una clave múltiple, y finalmente recorrer los resultados para extraer los nombres que cumplan con el presupuesto.

# === SOLUTION ===
def filtrar_ordenar_y_buscar(productos, presupuesto):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get("stock", 0) > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    disponibles.sort(key=lambda x: (x["precio"], x["nombre"]))
    
    # Buscar y extraer nombres de productos dentro del presupuesto
    resultado = [p["nombre"] for p in disponibles if p["precio"] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {"nombre": "Laptop", "precio": 1200, "stock": 5},
        {"nombre": "Mouse", "precio": 25, "stock": 10},
        {"nombre": "Teclado", "precio": 45, "stock": 0},
        {"nombre": "Monitor", "precio": 150, "stock": 2},
        {"nombre": "Audífonos", "precio": 45, "stock": 8}
    ]
    
    assert filtrar_ordenar_y_buscar(inventario, 50) == ["Mouse", "Audífonos"], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_y_buscar(inventario, 200) == ["Mouse", "Audífonos", "Monitor"], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_y_buscar(inventario, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")