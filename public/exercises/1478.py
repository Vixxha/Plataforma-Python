# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves "nombre", "precio" y "stock"). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, retornar una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para ordenar, y recorrer la lista resultante para extraer los nombres que cumplan con el presupuesto.

# === SOLUTION ===
def filtrar_ordenar_inventario(productos, presupuesto_maximo):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get("stock", 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x["precio"])
    
    # Filtrar y extraer nombres cuyo precio sea menor o igual al presupuesto máximo
    resultado = [p["nombre"] for p in ordenados if p["precio"] <= presupuesto_maximo]
    
    return resultado

# === TESTS ===
try:
    inventario_ejemplo = [
        {"nombre": "Mochila", "precio": 45.0, "stock": 5},
        {"nombre": "Lapicero", "precio": 1.5, "stock": 20},
        {"nombre": "Cuaderno", "precio": 3.0, "stock": 0},
        {"nombre": "Borrador", "precio": 0.5, "stock": 10}
    ]
    
    assert filtrar_ordenar_inventario(inventario_ejemplo, 5.0) == ["Borrador", "Lapicero"], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_inventario(inventario_ejemplo, 50.0) == ["Borrador", "Lapicero", "Mochila"], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_inventario(inventario_ejemplo, 0.4) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")