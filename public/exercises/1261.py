# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves "nombre", "precio" y "stock"). La función debe filtrar los productos cuyo stock sea mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista con los nombres de los primeros `n` productos resultantes (donde `n` es un parámetro dado). Si hay productos con el mismo precio, mantén su orden relativo original.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted (o el método sort) con una función lambda como key para el ordenamiento, y slicing para limitar la cantidad de elementos.

# === SOLUTION ===
def procesar_inventario(productos, n):
    productos_filtrados = [p for p in productos if p.get("stock", 0) > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x["precio"])
    nombres = [p["nombre"] for p in productos_ordenados[:n]]
    return nombres

# === TESTS ===
try:
    inventario_ejemplo = [
        {"nombre": "Mochila", "precio": 45.50, "stock": 10},
        {"nombre": "Borrador", "precio": 1.20, "stock": 0},
        {"nombre": "Lapicero", "precio": 1.50, "stock": 25},
        {"nombre": "Cuaderno", "precio": 3.80, "stock": 15}
    ]
    
    assert procesar_inventario(inventario_ejemplo, 2) == ["Lapicero", "Cuaderno"], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_ejemplo, 3) == ["Lapicero", "Cuaderno", "Mochila"], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")