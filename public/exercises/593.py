# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos alfabéticamente por nombre y busca el producto más barato entre ellos. Devuelve el nombre del producto filtrado más barato.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Usa un filtro (list comprehension), el método .sort() o sorted(), y la función min() con el parámetro 'key'.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['stock'] < 5]
    if not filtrados:
        return None
    filtrados.sort(key=lambda x: x['nombre'])
    producto_mas_barato = min(filtrados, key=lambda x: x['precio'])
    return producto_mas_barato['nombre']

# === TESTS ===
try:
    inventario = [
        {"nombre": "Monitor", "precio": 200, "stock": 10},
        {"nombre": "Mouse", "precio": 20, "stock": 2},
        {"nombre": "Teclado", "precio": 15, "stock": 3},
        {"nombre": "Webcam", "precio": 50, "stock": 1}
    ]
    assert procesar_inventario(inventario) == "Teclado", "Error: el test 1 ha fallado."
    assert procesar_inventario([{"nombre": "A", "precio": 10, "stock": 10}]) is None, "Error: el caso base falló."
    assert procesar_inventario([{"nombre": "Z", "precio": 5, "stock": 1}, {"nombre": "A", "precio": 5, "stock": 1}]) == "A", "Error: considera el ordenamiento alfabético al romper empates de precio."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")