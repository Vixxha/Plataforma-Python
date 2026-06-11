# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre' y 'precio'), filtra aquellos cuyo precio sea mayor o igual a un valor mínimo, ordénalos de forma ascendente por precio y devuelve solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor']
# hint: Puedes utilizar la función filter() o una lista por comprensión para filtrar, y el método sort() o la función sorted() con una llave lambda para ordenar.

# === SOLUTION ===
def filtrar_y_ordenar_productos(inventario, precio_minimo):
    # Filtrar productos que cumplen el precio mínimo
    filtrados = [p for p in inventario if p['precio'] >= precio_minimo]
    # Ordenar por precio de forma ascendente
    filtrados.sort(key=lambda x: x['precio'])
    # Retornar lista solo con los nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 15},
        {'nombre': 'Monitor', 'precio': 120},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Laptop', 'precio': 800}
    ]
    assert filtrar_y_ordenar_productos(inventario, 100) == ['Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 1000) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 0) == ['Mouse', 'Teclado', 'Monitor', 'Laptop'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")