# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre y precio), filtre aquellos cuyo precio sea menor o igual a un límite máximo, los ordene de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate) y finalmente devuelva una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el filtrado, el método sort() o la función sorted() con claves múltiples para el ordenamiento, y una comprensión final para extraer los nombres.

# === SOLUTION ===
def procesar_productos(productos, precio_maximo):
    filtrados = [p for p in productos if p['precio'] <= precio_maximo]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    catalogo = [
        {"nombre": "Queso", "precio": 15.0},
        {"nombre": "Pan", "precio": 2.5},
        {"nombre": "Leche", "precio": 2.5},
        {"nombre": "Manzana", "precio": 1.0},
        {"nombre": "Carne", "precio": 20.0}
    ]
    
    assert procesar_productos(catalogo, 5.0) == ["Manzana", "Leche", "Pan"], "Error: el test 1 ha fallado."
    assert procesar_productos(catalogo, 1.0) == ["Manzana"], "Error: considera casos límites en tu lógica."
    assert procesar_productos(catalogo, 0.5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")