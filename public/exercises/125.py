# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos cuyo precio sea menor a un límite dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Primero usa una comprensión de lista para filtrar por stock, luego ordena la lista resultante con sorted() usando una función lambda como clave, y finalmente aplica un último filtro para el precio.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    en_stock = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(en_stock, key=lambda x: x['precio'])
    resultado = [p['nombre'] for p in ordenados if p['precio'] < limite_precio]
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 0}
    ]
    assert procesar_inventario(inventario, 100) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 10) == [], "Error: debería devolver lista vacía si ningún producto cumple el precio."
    assert procesar_inventario([], 500) == [], "Error: el caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")