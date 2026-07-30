# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que procese una lista de diccionarios que representan productos. La función debe filtrar los productos cuyo precio sea menor o igual a un límite máximo, ordenarlos de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate) y finalmente buscar y retornar el nombre del primer producto que coincida con una categoría específica. Si no hay productos que cumplan con la categoría, debe retornar None.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Puedes usar la función `filter` o listas por comprensión para el filtrado, el método `sorted()` con una tupla como clave (`key`) para ordenar por múltiples criterios, y un bucle o condicional para la búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, precio_maximo, categoria_buscada):
    # Filtrar por precio máximo
    filtrados = [p for p in productos if p['precio'] <= precio_maximo]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Buscar el primer producto que coincida con la categoría buscada
    for producto in ordenados:
        if producto['categoria'] == categoria_buscada:
            return producto['nombre']
            
    return None

# === TESTS ===
try:
    inv = [
        {"nombre": "Laptop", "precio": 1200, "categoria": "Tecnología"},
        {"nombre": "Mouse", "precio": 25, "categoria": "Tecnología"},
        {"nombre": "Teclado", "precio": 45, "categoria": "Tecnología"},
        {"nombre": "Cafetera", "precio": 45, "categoria": "Hogar"}
    ]
    assert procesar_inventario(inv, 50, "Tecnología") == "Teclado", "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 30, "Tecnología") == "Mouse", "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv, 10, "Tecnología") is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")