import os
import json
import random
import urllib.request
import urllib.error

# La API key se inyecta por entorno (Variables Secretas en GitHub Actions)
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("Error: No se encontró la variable secreta GEMINI_API_KEY.")
    exit(1)

EXERCISES_DIR = os.path.join("public", "exercises")

# Crear el directorio si no existe
if not os.path.exists(EXERCISES_DIR):
    os.makedirs(EXERCISES_DIR)

# Averiguar cuál es el siguiente número disponible buscando los .py actuales
archivos = [f for f in os.listdir(EXERCISES_DIR) if f.endswith('.py')]
numeros = []
for f in archivos:
    try:
        numeros.append(int(f.split('.')[0]))
    except ValueError:
        pass

siguiente_num = max(numeros) + 1 if numeros else 1

temas = [
    "Manipulación de Strings (Cadenas)", 
    "Listas y Matrices (Vectores)", 
    "Diccionarios y Hashes", 
    "Algoritmos matemáticos básicos", 
    "Ordenamiento, Filtros y Búsqueda", 
    "Lógica Condicional e Iteración"
]
tema_elegido = random.choice(temas)

# Instrucciones muy estrictas para la IA
prompt = f"""
Escribe un único ejercicio de programación en Python sobre el tema: {tema_elegido}.
Nivel de dificultad: Básico-Intermedio.

El formato EXACTO de tu respuesta debe ser el siguiente bloque de código. Eres un bot de automatización, por tanto no incluyas ningún tipo de saludo, explicación ni notas antes o después del código. Tu respuesta completa será inyectada directamente en un archivo .py, por lo tanto si escribes texto que no es código dañarás la plataforma del estudiante.
Solo escribe este formato (Rellena los corchetes con el ejercicio):

# === METADATA ===
# title: [Título corto y llamativo]
# description: [Descripción clara y directa del problema algorítmico o manipulación de datos que hay que resolver]
# expected_output: [Un ejemplo de qué debería devolver u output]
# hint: [Una pista para ayudar al alumno (sin dar la solución directa)]

# === SOLUTION ===
def [nombre_de_tu_funcion]([parametros]):
    # tu solución real aquí, que pase los tests. Usa buenas prácticas.
    pass

# === TESTS ===
try:
    assert [nombre_de_tu_funcion]([arg1]) == [resultado1], "Error: el test 1 ha fallado."
    assert [nombre_de_tu_funcion]([arg2]) == [resultado2], "Error: considera casos límites en tu lógica."
    assert [nombre_de_tu_funcion]([arg3]) == [resultado3], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")
"""

import time

# ... (código existente ... el bucle irá aquí)
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key={API_KEY}"
headers = {'Content-Type': 'application/json'}
data = {
    "contents": [{"parts": [{"text": prompt}]}]
}
json_data = json.dumps(data).encode('utf-8')
request = urllib.request.Request(url, data=json_data, headers=headers)

max_reintentos = 3
for intento in range(max_reintentos):
    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
            texto_generado = result['candidates'][0]['content']['parts'][0]['text']
            
            # Limpiar si la IA encapsula la respuesta en bloques markdown
            texto_generado = texto_generado.strip()
            if texto_generado.startswith("```python"):
                texto_generado = texto_generado[9:]
            elif texto_generado.startswith("```"):
                 texto_generado = texto_generado[3:]
            if texto_generado.endswith("```"):
                texto_generado = texto_generado[:-3]
                
            texto_generado = texto_generado.strip()
            
            if "=== METADATA ===" not in texto_generado or "=== TESTS ===" not in texto_generado:
                print("El formato generado no es válido, cancelando guardado.")
                exit(1)

            nuevo_archivo_ruta = os.path.join(EXERCISES_DIR, f"{siguiente_num}.py")
            with open(nuevo_archivo_ruta, "w", encoding="utf-8") as file:
                file.write(texto_generado)
                
            print(f"Éxito: Se ha generado automáticamente {siguiente_num}.py sobre el tema '{tema_elegido}'.")
            break # Salir del bucle forzado porque tuvimos éxito
    except urllib.error.URLError as e:
        print(f"Intento {intento+1}/{max_reintentos} falló - Error: {e}")
        if hasattr(e, 'read'):
            cuerpo_error = e.read().decode('utf-8')
            print(cuerpo_error)
            if "503" not in str(e) and "503" not in cuerpo_error:
                exit(1) # Si el error es por otra cosa (ej: clave fallida 400), abortar inmediato
        
        if intento < max_reintentos - 1:
            print("Esperando 10 segundos antes del próximo intento por alta demanda...")
            time.sleep(10)
        else:
            print("Se alcanzó el número máximo de reintentos. La API está muy saturada hoy.")
            exit(1)
    except Exception as e:
        print(f"Excepción general: {e}")
        exit(1)
