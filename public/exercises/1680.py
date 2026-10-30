# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que procese una lista de diccionarios que representan productos. La función debe filtrar aquellos productos que tengan un precio menor o igual a un presupuesto dado, ordenarlos de forma descendente según su cantidad en stock, y finalmente buscar y devolver una lista con los nombres (en formato de cadena de texto) de los productos que coincidan exactamente con una categoría específica.
# difficulty: Intermedio
# expected_output: ['Manzanas', 'Peras']
# hint: Puedes usar list comprehensions o las funciones filter y sorted de Python, combinando condiciones de filtrado antes de extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto, categoria_buscada):
    # Filtrar por presupuesto
    filtrados = [p for p in productos if p["precio"] <= presupuesto]
    
    # Ordenar por stock de forma descendente
    ordenados = sorted(filtrados, key=lambda x: x["stock"], reverse=True)
    
    # Filtrar por categoría y extraer solo los nombres
    resultado = [p["nombre"] for p in ordenados if p["categoria"].lower() == categoria_buscada.lower()]
    
    return resultado

# === TESTS ===
try:
    inventario_ejemplo = [
        {"nombre": "Manzanas", "precio": 10.0, "stock": 50, "categoria": "Fruta"},
        {"nombre": "Peras", "precio": 15.0, "stock": 80, "categoria": "Fruta"},
        {"nombre": "Leche", "precio": 12.0, "stock": 30, "categoria": "Lácteos"},
        {"nombre": "Pan", "precio": 5.0, "stock": 100, "categoria": "Panadería"},
        {"nombre": "Queso", "precio": 25.0, "stock": 10, "categoria": "Lácteos"}
    ]
    
    assert procesar_inventario(inventario_ejemplo, 20.0, "Fruta") == ['Peras', 'Manzanas'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_ejemplo, 10.0, "Panadería") == ['Pan'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_ejemplo, 5.0, "Tecnología") == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")